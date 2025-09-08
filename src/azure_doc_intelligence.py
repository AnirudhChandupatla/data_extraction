from __future__ import annotations

import os
import logging
from typing import Optional, Iterable, Dict, Any, List, Tuple

from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, DocumentContentFormat

import markdownify


class AzureDocIntelligenceRunner:
    """
    Wraps Azure Document Intelligence for per-page analysis and Markdown conversion.
    - Loads endpoint/key from environment by default (AZURE_DOC_INTELLIGENCE_ENDPOINT, AZURE_DOC_INTELLIGENCE_KEY)
    - Analyzes one page at a time using 'prebuilt-layout' and returns Markdown
    - Resolves an internal logger compatible with ExtractionLogManager's hierarchy:
      e.g., 'extract' or 'extract.{extraction_id}.page.{page_num:04d}'
    """

    def __init__(
        self,
        *,
        # Credentials and endpoint
        endpoint: Optional[str] = None,
        api_key: Optional[str] = None,
        endpoint_env: str = "AZURE_DOC_INTELLIGENCE_ENDPOINT",
        key_env: str = "AZURE_DOC_INTELLIGENCE_KEY",
        # Analysis settings
        model_id: str = "prebuilt-layout",
        output_format: DocumentContentFormat = DocumentContentFormat.MARKDOWN,
        # Logger resolution compatible with ExtractionLogManager
        parent_logger_name: str = "extract",
        extraction_id: Optional[str] = None,
        page_num: Optional[int] = None,
    ) -> None:
        # Resolve endpoint/key
        self.endpoint = endpoint or os.getenv(endpoint_env)
        self.api_key = api_key or os.getenv(key_env)

        if not self.endpoint or not self.api_key:
            raise ValueError(
                "Azure Document Intelligence endpoint or key not provided; "
                "set via constructor or environment variables."
            )

        # Construct client
        self.client = DocumentIntelligenceClient(
            endpoint=self.endpoint,
            credential=AzureKeyCredential(self.api_key),
        )

        # Store config
        self.model_id = model_id
        self.output_format = output_format

        # Resolve a logger following ExtractionLogManager naming
        if extraction_id is not None and page_num is not None:
            logger_name = f"{parent_logger_name}.{extraction_id}.page.{page_num:04d}"
        else:
            logger_name = parent_logger_name
        self.logger = logging.getLogger(logger_name)

    # ---------- Core analysis ----------

    def analyze_page(self, page_bytes: bytes):
        """
        Submit a single-page PDF bytes for analysis and return the raw SDK result.
        """
        poller = self.client.begin_analyze_document(
            self.model_id,
            AnalyzeDocumentRequest(bytes_source=page_bytes),
            output_content_format=self.output_format,
        )
        result = poller.result()
        return result

    # ---------- Markdown conversion ----------

    @staticmethod
    def result_to_markdown(azure_doc_res) -> str:
        """
        Convert Azure result to Markdown:
        - Uses 'content' string
        - Splits on 'PageBreak' and converts the first segment with markdownify
        - Removes backslashes as in the original helper
        """
        pages = azure_doc_res.content.split("PageBreak")
        return markdownify.markdownify(pages[0], heading_style = 'ATX').replace("\\", '')

    def analyze_page_to_markdown(self, page_bytes: bytes) -> str:
        """
        Analyze a single page and return Markdown.
        """
        res = self.analyze_page(page_bytes)
        md = self.result_to_markdown(res)
        return md


'''
# Construct with environment-based credentials and align logger with a specific page
runner = AzureDocIntelligenceRunner(
    # endpoint and key will default from env: AZURE_DOC_INTELLIGENCE_ENDPOINT, AZURE_DOC_INTELLIGENCE_KEY
    model_id="prebuilt-layout",
    parent_logger_name="extract",
    extraction_id="abcd-1234",
    page_num=1,
)

# Single page
markdown_str = runner.analyze_page_to_markdown(page_bytes)  # bytes of a single-page PDF
'''