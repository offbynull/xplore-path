from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.nodes.filesystem.file_loader import FileLoader, NODE_CREATOR


class CombinedFileLoader(FileLoader):
    """
    ``FileLoader`` that combines several ``FileLoader``\s under one umbrella. When loading a file, each inner
    `FileLoader`` is invoked until one succeeds.
    """
    def __init__(self, loaders: list[FileLoader]):
        """
        Construct a ``CombinedFileLoader`` object.

        :param loaders: Inner ``FileLoader``\s.
        """
        self.loaders = loaders

    def is_loadable(self, p: pathlib.Path) -> bool:
        return any(l.is_loadable(p) for l in self.loaders)

    def is_cachable(self, p: pathlib.Path) -> bool:
        return next(l.is_cachable(p) for l in self.loaders if l.is_loadable(p))

    def node_creator(self, p: pathlib.Path) -> NODE_CREATOR:
        return next(l.node_creator(p) for l in self.loaders if l.is_loadable(p))

    def load(self, p: pathlib.Path) -> Any:
        for l in self.loaders:
            if l.is_loadable(p):
                try:
                    return l.load(p)
                except Exception:
                    ...
        return None
