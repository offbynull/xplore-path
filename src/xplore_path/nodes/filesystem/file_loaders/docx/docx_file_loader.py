from __future__ import annotations

import pathlib
from typing import Any

from docx import Document

from xplore_path.nodes.filesystem.file_loader import FileLoader


class DocxFileLoader(FileLoader):
    """
    ``FileLoader`` for Microsoft Word files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.docx'

    def load(self, p: pathlib.Path) -> Any:
        doc = Document(str(p))
        return '\n\n'.join(paragraph.text for paragraph in doc.paragraphs)
