from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.nodes.filesystem.file_loader import FileLoader, PATH_LOADER
from xplore_path.nodes.filesystem.file_loaders.sqlite.sqlite_object_path import SqliteObjectNode


class SqliteFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        try:
            with p.open('rb') as file:
                return file.read(16) == b'SQLite format 3\x00'
        except IOError:
            return False

    def is_cachable(self, p: pathlib.Path) -> bool:
        return False

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return SqliteObjectNode

    def load(self, p: pathlib.Path) -> Any:
        return p
