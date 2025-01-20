from __future__ import annotations

import pathlib
from typing import Any

from PyPDF2 import PdfReader

from xplore_path.nodes.filesystem.file_loader import FileLoader


class PdfFileLoader(FileLoader):
    """
    ``FileLoader`` for PDF files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.pdf'

    def load(self, p: pathlib.Path) -> Any:
        reader = PdfReader(p)
        return {reader.get_page_number(page): page.extract_text() for page in reader.pages}
