import os, uno, time
from flask import Flask, request, jsonify
from com.sun.star.beans import PropertyValue
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


desktop = None


def get_desktop(retries: int = 10, delay: float = 1.0):
    """
    Lazily initialize + cache a UNO desktop, retrying until office is up.
    """
    global desktop
    if desktop is None:
        for i in range(retries):
            try:
                local_ctx = uno.getComponentContext()
                resolver = local_ctx.ServiceManager.createInstanceWithContext(
                    "com.sun.star.bridge.UnoUrlResolver", local_ctx)
                ctx = resolver.resolve(
                    "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
                sm = ctx.ServiceManager
                desktop = sm.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
                break
            except Exception as e:
                if i == retries - 1:
                    raise RuntimeError("Could not connect to UNO after retries") from e
                time.sleep(delay)
    return desktop


def extract_text_from_pdf_with_original_layout(pdf_path, char_unit=50, max_spaces=10, y_tolerance=100):
    """
    Load the given PDF via the pre-warmed UNO desktop,
    extract text (preserving original layout), then close.
    
    Parameters:
    - char_unit: Units per character position (higher = fewer spaces, lower = more spaces)
    - max_spaces: Maximum consecutive spaces to add between text elements
    - y_tolerance: Tolerance for grouping shapes on the same row
    """
    dsk = get_desktop()
    file_url = uno.systemPathToFileUrl(os.path.abspath(pdf_path))
    props = (
        PropertyValue("Hidden", 0, True, 0),
        PropertyValue("FilterName", 0, "writer_pdf_import", 0),
    )
    doc = dsk.loadComponentFromURL(file_url, "_blank", 0, props)
    extracted = []


    # if it were a text doc (rare for PDF) ...
    if hasattr(doc, "Text"):
        cursor = doc.Text.createTextCursor()
        extracted.append(cursor.getString())
    else:
        # most PDFs come in as a DrawDocument
        raw_shapes = []


        pages = doc.getDrawPages()
        for p in range(pages.getCount()):
            page = pages.getByIndex(p)
            for s in range(page.getCount()):
                shape = page.getByIndex(s)
                try:
                    txt = shape.getString()
                    if not txt:
                        continue
                    pos = shape.getPosition()
                    size = shape.getSize()
                    raw_shapes.append((pos.X, pos.Y, size.Width, txt))
                except AttributeError:
                    pass


        if not raw_shapes:
            doc.close(True)
            return ""


        grid: dict[int, dict[int, str]] = {}
        for x, y, _, txt in raw_shapes:
            row = round(y / y_tolerance)
            col = round(x / char_unit)  # Using configurable char_unit
            grid.setdefault(row, {})[col] = txt


        ordered_lines: list[str] = []
        for row in sorted(grid):
            cols = grid[row]
            cursor = 0
            pieces = []
            for col in sorted(cols):
                if col > cursor:
                    # Limit the number of spaces added
                    spaces_to_add = min(col - cursor, max_spaces)
                    pieces.append(" " * spaces_to_add)
                pieces.append(cols[col])
                cursor = col + len(cols[col])
            ordered_lines.append("".join(pieces))


        extracted.append("\n".join(ordered_lines))


    doc.close(True)
    return "\n".join(extracted)


@app.route('/read_pdf_text', methods=['POST'])
def read_file():
    f = request.files.get('file')
    if not f or f.filename == '':
        return jsonify(error="No file"), 400
    
    '''
    char_unit parameter: Controls the spacing calculation. Higher values result in fewer spaces, lower values result in more spaces.

    max_spaces parameter: Limits the maximum number of consecutive spaces that can be added between text elements, preventing excessive whitespace.

    y_tolerance parameter: Makes the row grouping tolerance configurable.
    '''

    # Get spacing parameters from request
    char_unit = request.form.get('char_unit', 50, type=int)
    max_spaces = request.form.get('max_spaces', 10, type=int)
    y_tolerance = request.form.get('y_tolerance', 100, type=int)
    
    fn = secure_filename(f.filename)
    dest = os.path.join(app.config['UPLOAD_FOLDER'], fn)
    f.save(dest)
    try:
        txt = extract_text_from_pdf_with_original_layout(
            dest, 
            char_unit=char_unit, 
            max_spaces=max_spaces, 
            y_tolerance=y_tolerance
        )
    finally:
        os.remove(dest)
    return jsonify(extracted_text=txt), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
