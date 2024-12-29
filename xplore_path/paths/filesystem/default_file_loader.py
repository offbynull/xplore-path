from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.paths.filesystem.file_loader import FileLoader


class DefaultFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return True

    def load(self, p: pathlib.Path) -> Any:
        try:
            return p.read_text(encoding='US-ASCII')
        except Exception:
            return []
