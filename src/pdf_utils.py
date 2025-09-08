import os
import io
import base64
from typing import Optional, Tuple, List, Dict, Any

import requests
from tqdm import tqdm
from pdf2image import convert_from_bytes
from pikepdf import Pdf


class PDFTextAndImageExtractor:
    """
    Extract per-page text and images from a PDF using a local text-extraction API
    and pdf2image for rendering, preserving the original behavior from the script.

    Attributes
    ----------
    api_url : str
        Base URL or full endpoint to the text extraction API. If a base URL is given,
        '/read_pdf_text' will be appended automatically.
    char_unit : int
        Character unit parameter forwarded to the API as string (compat with original).
    max_spaces : int
        Max spaces parameter forwarded to the API as string.
    y_tolerance : int
        Y tolerance parameter forwarded to the API as string.
    timeout : Tuple[float, float]
        (connect, read) timeout for the API request.
    dpi : int
        Rendering DPI for pdf2image.
    session : requests.Session
        Reused HTTP session for efficiency.
    """

    def __init__(
        self,
        api_url: str = "http://localhost:5000/read_pdf_text",
        *,
        char_unit: int = 100,
        max_spaces: int = 200,
        y_tolerance: int = 100,
        timeout: Tuple[float, float] = (10, 120),
        dpi: int = 600,
        session: Optional[requests.Session] = None,
    ) -> None:
        self.api_url = api_url.rstrip("/")
        self.char_unit = char_unit
        self.max_spaces = max_spaces
        self.y_tolerance = y_tolerance
        self.timeout = timeout
        self.dpi = dpi
        self.session = session or requests.Session()

    def _resolve_endpoint(self) -> str:
        """Resolve full endpoint, allowing either base URL or full path."""
        if self.api_url.endswith("/read_pdf_text"):
            return self.api_url
        return f"{self.api_url}/read_pdf_text"

    def _post_page(self, page_bytes: bytes, filename: str) -> Dict[str, Any]:
        """
        Send one page to the text-extraction endpoint as multipart/form-data and return JSON.
        """
        files = {"file": (filename, io.BytesIO(page_bytes), "application/pdf")}
        data = {
            "char_unit": str(self.char_unit),
            "max_spaces": str(self.max_spaces),
            "y_tolerance": str(self.y_tolerance),
        }
        r = self.session.post(self._resolve_endpoint(), data=data, files=files, timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    @staticmethod
    def _pdf_obj_to_bytes(pdf_obj) -> bytes:
        """
        Convert a pikepdf page object into a standalone PDF bytes buffer.
        """
        dst = Pdf.new()
        # Copy page object (preserves text layer)
        dst.pages.append(pdf_obj)
        buf = io.BytesIO()
        dst.save(buf)
        return buf.getvalue()

    def _render_page_png_base64(self, page_bytes: bytes):
        """
        Render a page to a PIL Image and return the image and its base64-encoded PNG.
        """
        images = convert_from_bytes(
            page_bytes,
            dpi=self.dpi,
            single_file=True,
        )
        buffered = io.BytesIO()
        images[0].save(buffered, format="PNG", optimize=True)
        img_bytes = buffered.getvalue()
        img_base64 = base64.b64encode(img_bytes).decode("utf-8")
        return images[0], img_base64

    def process_pdf(
        self,
        pdf_path: str,
        *,
        include_pil_image: bool = True,
        include_base64: bool = True,
        show_progress: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Process all pages of a PDF on disk.

        Returns a list of dicts with:
          - page_number: int
          - page_bytes: bytes
          - pil_image: PIL.Image.Image | None
          - base64_image: str | None
          - full_text: str
        """
        src = Pdf.open(pdf_path)
        n_pages = len(src.pages)
        results: List[Dict[str, Any]] = []

        iterator = range(n_pages)
        if show_progress:
            iterator = tqdm(iterator, total=n_pages, desc="Processing pages")

        pg_filename = os.path.basename(pdf_path)
        pg_file_name_without_ext = os.path.splitext(pg_filename)[0]

        for pg in iterator:
            pdf_page_obj = src.pages[pg]
            pg_bytes = self._pdf_obj_to_bytes(pdf_page_obj)

            pil_image = None
            base64_image = None
            if include_pil_image or include_base64:
                pil_image, base64_image = self._render_page_png_base64(pg_bytes)

            res = self._post_page(page_bytes=pg_bytes, filename=pg_file_name_without_ext + ".pdf")

            results.append({
                "page_number": pg + 1,
                "page_bytes": pg_bytes,
                "pil_image": pil_image if include_pil_image else None,
                "base64_image": base64_image if include_base64 else None,
                "full_text": res.get("extracted_text", ""),
            })

        return results

    def process_pdf_bytes(
        self,
        pdf_bytes: bytes,
        *,
        filename_stub: str = "document",
        include_pil_image: bool = True,
        include_base64: bool = True,
        show_progress: bool = True,
    ) -> List[Dict[str, Any]]:
        """
        Process all pages of a PDF provided as bytes (convenience for in-memory use).
        """
        src = Pdf.open(io.BytesIO(pdf_bytes))
        n_pages = len(src.pages)
        results: List[Dict[str, Any]] = []

        iterator = range(n_pages)
        if show_progress:
            iterator = tqdm(iterator, total=n_pages, desc="Processing pages")

        for pg in iterator:
            pdf_page_obj = src.pages[pg]
            pg_bytes = self._pdf_obj_to_bytes(pdf_page_obj)

            pil_image = None
            base64_image = None
            if include_pil_image or include_base64:
                pil_image, base64_image = self._render_page_png_base64(pg_bytes)

            res = self._post_page(page_bytes=pg_bytes, filename=filename_stub + ".pdf")

            results.append({
                "page_number": pg + 1,
                "page_bytes": pg_bytes,
                "pil_image": pil_image if include_pil_image else None,
                "base64_image": base64_image if include_base64 else None,
                "full_text": res.get("extracted_text", ""),
            })

        return results
