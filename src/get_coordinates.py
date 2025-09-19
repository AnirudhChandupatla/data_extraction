import fitz  # PyMuPDF
from collections import defaultdict
import json

def extract_and_format_pdf(pdf_path, y_threshold=2.0, normalize_coords=False):
    """
    Extracts words, processes them into sorted lines, and formats the output
    with an option to normalize coordinates.

    Args:
        pdf_path (str): The path to the PDF file.
        y_threshold (float): The maximum vertical distance for words to be
                             considered on the same line.
        normalize_coords (bool): If True, normalizes coordinates to a 0-1 scale
                                 based on page dimensions.

    Returns:
        dict: A dictionary where keys are page numbers and values are lists of
              lines, with each line containing formatted word dictionaries.
    """
    # 1. Extract all words and get page dimensions
    try:
        doc = fitz.open(pdf_path)
        all_words = []
        page_dimensions = {}  # To store width and height for each page

        for page_num, page in enumerate(doc):
            # Get page dimensions for normalization
            rect = page.rect
            page_dimensions[page_num + 1] = (rect.width, rect.height)

            word_list = page.get_text("words")
            all_words.extend([word + (page_num + 1,) for word in word_list])
        doc.close()
    except Exception as e:
        print(f"Error opening or reading PDF '{pdf_path}': {e}")
        return None

    # 2. Group words by page number
    pages = defaultdict(list)
    for word_data in all_words:
        pages[word_data[8]].append(word_data)

    # 3. Process each page
    processed_pages = {}
    for page_num, words in pages.items():
        if not words:
            processed_pages[page_num] = []
            continue

        words_sorted_by_y = sorted(words, key=lambda w: w[1])

        lines = []
        current_line = [words_sorted_by_y[0]]
        for word in words_sorted_by_y[1:]:
            if abs(word[1] - current_line[0][1]) <= y_threshold:
                current_line.append(word)
            else:
                lines.append(current_line)
                current_line = [word]
        lines.append(current_line)

        # 4. Sort words in lines and apply final formatting
        page_width, page_height = page_dimensions[page_num]
        final_lines = []
        for line in lines:
            sorted_line = sorted(line, key=lambda w: w[0])
            
            formatted_line = []
            for word in sorted_line:
                x0, y0, x1, y1, text, *_ = word
                
                # Conditionally normalize coordinates
                if normalize_coords:
                    poly = [
                        x0 / page_width,
                        y0 / page_height,
                        x1 / page_width,
                        y1 / page_height
                    ]
                else:
                    poly = [x0, y0, x1, y1]
                
                formatted_line.append({
                    "text": text,
                    "polygon": poly
                })
            final_lines.append(formatted_line)
            
        processed_pages[page_num] = final_lines

    return processed_pages

# --- Example Usage ---
pdf_file = "your_native_document.pdf"

# --- 1. Get Native (Absolute) Coordinates ---
print("--- Generating results with NATIVE coordinates ---")
native_result = extract_and_format_pdf(pdf_file, normalize_coords=False)
if native_result:
    print(json.dumps(native_result, indent=2))

print("\n" + "="*50 + "\n")

# --- 2. Get Normalized Coordinates ---
print("--- Generating results with NORMALIZED coordinates ---")
normalized_result = extract_and_format_pdf(pdf_file, normalize_coords=True)
if normalized_result:
    print(json.dumps(normalized_result, indent=2))
