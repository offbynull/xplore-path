from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.nodes.filesystem.file_loader import FileLoader, PATH_LOADER


class CombinedFileLoader(FileLoader):
    def __init__(self, loaders: list[FileLoader]):
        self.loaders = loaders

    def is_loadable(self, p: pathlib.Path) -> bool:
        return any(l.is_loadable(p) for l in self.loaders)

    def is_cachable(self, p: pathlib.Path) -> bool:
        return next(l.is_cachable(p) for l in self.loaders if l.is_loadable(p))

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return next(l.path_creator(p) for l in self.loaders if l.is_loadable(p))

    def load(self, p: pathlib.Path) -> Any:
        for l in self.loaders:
            if l.is_loadable(p):
                try:
                    return l.load(p)
                except Exception:
                    ...
        return None
