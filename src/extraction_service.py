import logging
import json
import pandas as pd
from pathlib import Path
from pdf_utils import PDFTextAndImageExtractor
from log_utils import ExtractionLogManager
from azure_doc_intelligence import AzureDocIntelligenceRunner
from openai_utils import AzureResponsesClient
from agent_prompts import human_reviewed_schema, table_grid_emptiness, extractor_with_feedback, judge, extractor, OCR_content_filter, coordinate_based_empty_cell_finder
import itertools

def prepare_table_feedback(issues):
    return '\n'.join([f'''Issue {i+1}:
row: {issue['row']}
column: {issue['column']}
{issue['feedback']}
-------------''' for i,issue in enumerate(issues)])

def iter_dict_chunks(d, n):
    it = iter(d.items())
    while True:
        chunk_items = list(itertools.islice(it, n))
        if not chunk_items:
            break
        yield dict(chunk_items)

# --- new import near other imports ---
from joblib import Parallel, delayed

# ... existing imports and helpers ...
# import logging, json, pandas as pd, Path, PDFTextAndImageExtractor, ExtractionLogManager, AzureDocIntelligenceRunner, AzureResponsesClient, agent prompts, itertools ...

# add near other imports
import re
import ast

def _strip_code_fences(s: str) -> str:
    """
    Remove a single fenced Markdown code block if present, preserving inner text.
    """
    if not s:
        return s
    m = re.search(r"``````", s)
    return m.group(1) if m else s

def _extract_first_bracket_block(s: str) -> str:
    """
    Return the first balanced {...} or [...] block to ignore preambles/epilogues.
    """
    if not s:
        return s
    start_obj = s.find("{")
    start_arr = s.find("[")
    starts = [i for i in (start_obj, start_arr) if i != -1]
    if not starts:
        return s.strip()
    start = min(starts)
    stack = []
    for i, ch in enumerate(s[start:], start):
        if ch in "{[":
            stack.append(ch)
        elif ch in "}]":
            if not stack:
                break
            opener = stack.pop()
            if (opener == "{" and ch != "}") or (opener == "[" and ch != "]"):
                # mismatched but keep scanning
                pass
            if not stack:
                return s[start:i + 1]
    return s[start:].strip()

def parse_llm_json(text: str):
    """
    Robustly parse LLM 'JSON' that may be:
    - fenced in ``````
    - prefixed/suffixed with prose
    - single-quoted Python-literals

    Strategy: strip fences -> extract first balanced block -> json.loads -> ast.literal_eval.
    """
    raw = _strip_code_fences(text or "").strip()
    raw = _extract_first_bracket_block(raw)
    # Try strict JSON first
    try:
        return json.loads(raw)
    except Exception:
        pass
    # Fallback to safe Python literal parsing
    try:
        return ast.literal_eval(raw)
    except Exception:
        logging.getLogger("extract").exception("Failed to parse LLM output as JSON/Python literal")
        # Best-effort neutral default to keep pipeline moving
        return {} if raw.startswith("{") else []

def process_one_page(page_idx1: int,
                     page_data: dict,
                     extraction_id: str,
                     root: Path,
                     judge_retry_max_attempts: int) -> int:
    """
    Process a single page (1-based index) in its own process:
    - sets up per-page logger
    - runs initial extraction
    - runs judge / correction loops for form fields and tables
    - writes original_extraction.json and corrected_extraction.json
    """
    # Recreate a logger manager in this worker process
    mgr = ExtractionLogManager(
        base_dir=Path("./runs"),
        parent_logger_name="extract",
        level=logging.INFO,
        enable_console=True,
        console_format="%(asctime)s | %(levelname)s | %(message)s",
    )

    with mgr.page_logger(root, extraction_id, page_num=page_idx1) as (logger, page_dir):
        logger.info('started initial extraction for page %s', page_idx1)

        openai_client = AzureResponsesClient(
            model=extractor['model'],
            extraction_id=extraction_id,
            page_num=page_idx1,
        )

        # minimal page payload expected: full_text, base64_image, page_bytes
        initial_extraction_response = openai_client.invoke(
            page_data['full_text'],
            page_data['base64_image'],
            system_prompt=extractor['system_prompt'],
            user_prompt=extractor['user_prompt'],
            reasoning_effort=extractor['reasoning_effort'],
            model=extractor['model'],
            data_type='FULL_RAW_TEXT',
        )

        # safer than eval
        initial_text = openai_client.extract_response_text(initial_extraction_response) or "{}"
        extracted_data = parse_llm_json(initial_text)

        logger.info('initial extraction of page data done.')
        with (page_dir / "original_extraction.json").open("w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=2, ensure_ascii=False)

        # ==== PROCESSING EACH PAGE'S EXTRACTED DATA ====
        for data_part in extracted_data.keys():
            if data_part == 'Form_fields':  # should match human_reviewed_schema key
                logger.info('started validating form fields')

                # processing 10 form fields at a time
                for field_subset in iter_dict_chunks(extracted_data[data_part], 10):
                    field_list = list(field_subset.keys())
                    logger.info('-validating form fields: %s', field_list)
                    logger.info('--current are:\n%s', '\n'.join([k + ' : ' + (v or '') for k, v in field_subset.items()]))
                    
                    judge_retry_attempt = 1
                    while judge_retry_attempt <= judge_retry_max_attempts:
                        if judge_retry_attempt > 1:
                            logger.info('-revalidating form fields: %s', field_list)

                        judge_agent = judge.copy()
                        judge_agent['user_prompt'] = (judge_agent['user_prompt']
                            .replace('DATA_PART_INSTRUCTIONS', judge_agent['form_field_instructions'])
                            .replace('DATA_PART', data_part)
                            .replace('DATA_NAME', '')
                            .replace('DATA_VALUE', '\n'.join([k + ':' + (v or '') for k, v in field_subset.items()]))
                            .replace('## GRID_INFO:', '')
                            .replace('OUTPUT_FORMAT', judge_agent['form_field_output_format'])
                        )

                        judge_response = openai_client.invoke(
                            page_data['full_text'],
                            page_data['base64_image'],
                            system_prompt=judge_agent['system_prompt'],
                            user_prompt=judge_agent['user_prompt'],
                            reasoning_effort=judge_agent['reasoning_effort'],
                            model=judge_agent['model'],
                            data_type='FULL_RAW_TEXT',
                        )

                        form_field_text = openai_client.extract_response_text(judge_response) or "[]"
                        form_field_feedback = parse_llm_json(form_field_text)
                        form_field_issues = [ff for ff in form_field_feedback if ff.get('status') == 'wrong']

                        if form_field_issues:
                            logger.info('--found issues: %s', form_field_issues)
                            judge_retry_attempt += 1

                            form_field_feedback_string = '\n'.join(
                                [ffi['data_name'] + ':' + ffi.get('feedback', '') for ffi in form_field_issues]
                            )

                            extractor_with_feedback_agent = extractor_with_feedback.copy()
                            extractor_with_feedback_agent['user_prompt'] = (extractor_with_feedback_agent['user_prompt']
                                .replace('DATA_PART', data_part)
                                .replace('DATA_VALUE', '\n'.join([k + ':' + (v or '') for k, v in field_subset.items()]))
                                .replace('FEEDBACK', form_field_feedback_string)
                                .replace('OUTPUT_FORMAT', extractor_with_feedback_agent['form_field_output_format'])
                                .replace('DATA_NAME', '')
                            )

                            extractor_with_feedback_response = openai_client.invoke(
                                page_data['full_text'],
                                page_data['base64_image'],
                                system_prompt=extractor_with_feedback_agent['system_prompt'],
                                user_prompt=extractor_with_feedback_agent['user_prompt'],
                                reasoning_effort=extractor_with_feedback_agent['reasoning_effort'],
                                model=extractor_with_feedback_agent['model'],
                                data_type='FULL_RAW_TEXT',
                            )

                            correction_text = openai_client.extract_response_text(extractor_with_feedback_response) or "{}"
                            extracted_data_correction = parse_llm_json(correction_text)

                            logger.info('--corrected as:\n%s', '\n'.join([k + ' : ' + (v or '') for k, v in extracted_data_correction.items()]))

                            field_subset.update(extracted_data_correction)
                        else:
                            logger.info('done judging, ALL GOOD')
                            break

                    extracted_data[data_part].update(field_subset)

            if data_part == 'Tables':
                # get markdown from Azure Document Intelligence only for tables
                runner = AzureDocIntelligenceRunner(
                    model_id="prebuilt-layout",
                    parent_logger_name="extract",
                    extraction_id=extraction_id,
                    page_num=page_idx1,
                )

                # markdown_str = runner.analyze_page_to_markdown(page_data['page_bytes'])
                azure_doc_res = runner.analyze_page(page_data['page_bytes'])
                relavent_ocr_info = []
                for element in azure_doc_res['pages'][0]['lines']:
                    _ = element.pop('spans', 'Key not found')
                    relavent_ocr_info.append(element)
                
                logger.info('got response with OCR coordinates info from azure doc intelligence for page %s', page_idx1)
                logger.info('started validating tables')

                # processing 1 table at a time
                for table in iter_dict_chunks(extracted_data[data_part], 1):
                    table_name, table_data = table.popitem()
                    df = pd.DataFrame(table_data)
                    table_mrk_str = df.to_markdown(index=False)
                    logger.info('-current table:\n%s', table_mrk_str)
                    logger.info('-validating table: %s', table_name)

                    if not table_data:
                        continue  # if table is empty do not check

                    logger.info('--figuring out table emptiness...')
                    # grid_emptiness_agent = table_grid_emptiness.copy()
                    # grid_emptiness_agent['user_prompt'] = (grid_emptiness_agent['user_prompt']
                    #     .replace('TABLE_NAME', table_name)
                    #     .replace('TABLE_COLUMNS', str(human_reviewed_schema[data_part][table_name]))
                    # )

                    # grid_emptiness_response = openai_client.invoke(
                    #     markdown_str,
                    #     page_data['base64_image'],
                    #     system_prompt=grid_emptiness_agent['system_prompt'],
                    #     user_prompt=grid_emptiness_agent['user_prompt'],
                    #     reasoning_effort=grid_emptiness_agent['reasoning_effort'],
                    #     model=grid_emptiness_agent['model'],
                    #     data_type='MARKDOWN',
                    # )
                    # grid_emptiness_info = openai_client.extract_response_text(grid_emptiness_response) or ""

                    ocr_agent = OCR_content_filter.copy()
                    ocr_agent['user_prompt'] = (ocr_agent['user_prompt']
                        .replace('TABLE_NAME', table_name)
                        .replace('TABLE_CONTENT', table_mrk_str)
                    )

                    table_relate_filtered_ocr_response = openai_client.invoke(
                        str(relavent_ocr_info),
                        page_data['base64_image'],
                        system_prompt=ocr_agent['system_prompt'],
                        user_prompt=ocr_agent['user_prompt'],
                        reasoning_effort=ocr_agent['reasoning_effort'],
                        model=ocr_agent['model'],
                        data_type='OCR_COORDINATES',
                    )

                    table_relate_filtered_ocr_info = openai_client.extract_response_text(table_relate_filtered_ocr_response) or ""
                    logger.info('--got table related OCR content from Azure Doc Intelligence')

                    table_grid_emptiness_agent = coordinate_based_empty_cell_finder.copy()
                    table_grid_emptiness_agent['user_prompt'] = (table_grid_emptiness_agent['user_prompt']
                        .replace('OCR_CONTENT', table_relate_filtered_ocr_info)
                        .replace('TABLE_NAME', table_name)
                        .replace('COLUMN_HEADERS', '|' + '|'.join(human_reviewed_schema[data_part][table_name]) + '|')
                    )

                    table_grid_emptiness_response = openai_client.invoke(
                        None,
                        None,
                        system_prompt=table_grid_emptiness_agent['system_prompt'],
                        user_prompt=table_grid_emptiness_agent['user_prompt'],
                        reasoning_effort=table_grid_emptiness_agent['reasoning_effort'],
                        model=table_grid_emptiness_agent['model'],
                        data_type=None,
                    )
                    
                    table_grid_emptiness_info = openai_client.extract_response_text(table_grid_emptiness_response) or ""
                    logger.info('--got table grid emptiness info:\n%s', table_grid_emptiness_info)

                    judge_retry_attempt = 1
                    while judge_retry_attempt <= judge_retry_max_attempts:
                        if judge_retry_attempt > 1:
                            logger.info('-revalidating table: %s', table_name)
                            df = pd.DataFrame(table_data)
                            table_mrk_str = df.to_markdown(index=False)

                        judge_agent = judge.copy()

                        judge_agent['user_prompt'] = (judge_agent['user_prompt']
                            .replace('DATA_PART_INSTRUCTIONS', judge_agent['table_instructions'])
                            .replace('DATA_PART', data_part)
                            .replace('DATA_NAME', table_name)
                            .replace('DATA_VALUE', table_mrk_str)
                            .replace('## GRID_INFO:', f"## GRID_INFO (tells whether a cell is empty or not, non empty cells are marked as 'X', trusted since calculated using OCR coordinates) :\n{table_grid_emptiness_info}\n")
                            .replace('OUTPUT_FORMAT', judge_agent['table_output_format'])
                        )

                        judge_response = openai_client.invoke(
                            page_data['full_text'],
                            page_data['base64_image'],
                            system_prompt=judge_agent['system_prompt'],
                            user_prompt=judge_agent['user_prompt'],
                            reasoning_effort=judge_agent['reasoning_effort'],
                            model=judge_agent['model'],
                            data_type='FULL_RAW_TEXT',
                        )

                        tables_text = openai_client.extract_response_text(judge_response) or "[]"
                        tables_feedback = parse_llm_json(tables_text)
                        tables_issues = [t_issue for t_issue in tables_feedback if t_issue.get('status') == 'wrong']

                        if tables_issues:
                            logger.info('--found issues: %s', tables_issues)
                            judge_retry_attempt += 1

                            table_feedback_string = prepare_table_feedback(tables_issues)

                            extractor_with_feedback_agent = extractor_with_feedback.copy()
                            extractor_with_feedback_agent['user_prompt'] = (extractor_with_feedback_agent['user_prompt']
                                .replace('DATA_PART', data_part)
                                .replace('DATA_VALUE', table_mrk_str)
                                .replace('FEEDBACK', table_feedback_string)
                                .replace('OUTPUT_FORMAT', extractor_with_feedback_agent['table_output_format'])
                                .replace('DATA_NAME', table_name)
                            )

                            extractor_with_feedback_response = openai_client.invoke(
                                page_data['full_text'],
                                page_data['base64_image'],
                                system_prompt=extractor_with_feedback_agent['system_prompt'],
                                user_prompt=extractor_with_feedback_agent['user_prompt'],
                                reasoning_effort=extractor_with_feedback_agent['reasoning_effort'],
                                model=extractor_with_feedback_agent['model'],
                                data_type='FULL_RAW_TEXT',
                            )

                            correction_text = openai_client.extract_response_text(extractor_with_feedback_response) or "[]"
                            extracted_data_correction = parse_llm_json(correction_text)

                            logger.info('--corrected as:\n%s', pd.DataFrame(extracted_data_correction).to_markdown(index=False))

                            table_data = extracted_data_correction  # update old data with new corrected data
                            table.update({table_name: table_data})
                        else:
                            logger.info('done judging, ALL GOOD')
                            break

                    extracted_data[data_part].update(table)

        with (page_dir / "corrected_extraction.json").open("w", encoding="utf-8") as f:
            json.dump(extracted_data, f, indent=2, ensure_ascii=False)

    return page_idx1

if __name__ == "__main__":  # critical for multiprocessing on Windows/macOS
    # Extract PIL image, full text, bytes, base64 image from a PDF file
    pdf_extractor = PDFTextAndImageExtractor()
    per_page_text_and_images = pdf_extractor.process_pdf('obfuscated_fake_cbiz_prof_10_pages.pdf')

    mgr = ExtractionLogManager(base_dir=Path("./runs"),
                               parent_logger_name="extract",
                               level=logging.INFO,
                               enable_console=True)

    # Create a unique extraction root
    extraction_id, root = mgr.create_extraction_root()

    judge_retry_max_attempts = 3

    # Build tasks: keep only the fields the worker needs to reduce pickling overhead
    tasks = []
    for idx1, pg in enumerate(per_page_text_and_images, start=1):
        tasks.append((
            idx1,
            {
                "page_bytes": pg["page_bytes"],
                "full_text": pg["full_text"],
                "base64_image": pg["base64_image"],
            },
            extraction_id,
            root,
            judge_retry_max_attempts,
        ))

    # Parallel execution (process-based via loky backend)
    Parallel(n_jobs=3, backend="loky")(
        delayed(process_one_page)(*t) for t in tasks
    )
