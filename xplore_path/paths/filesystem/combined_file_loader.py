from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.paths.filesystem.file_loader import FileLoader


class CombinedFileLoader(FileLoader):
    def __init__(self, loaders: list[FileLoader]):
        self.loader = loaders

    def is_loadable(self, p: pathlib.Path) -> bool:
        return any(l.is_loadable(p) for l in self.loader)

    def load(self, p: pathlib.Path) -> Any:
        for l in self.loader:
            if l.is_loadable(p):
                try:
                    return l.load(p)
                except Exception:
                    ...
        return None
