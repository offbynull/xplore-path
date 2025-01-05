from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.paths.filesystem.file_loader import FileLoader


class TextFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.txt'

    def load(self, p: pathlib.Path) -> Any:
        return {'content': p.read_text(encoding='utf-8')}
