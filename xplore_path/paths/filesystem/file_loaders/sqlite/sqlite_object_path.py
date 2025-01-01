from __future__ import annotations

import pathlib
import sqlite3
from typing import Hashable

from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class SqliteTablePath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            fs_path: pathlib.Path,
    ):
        super().__init__(parent, position_in_parent, label, None)
        self.fs_path = fs_path

    def all_children(self) -> list[Path]:
        with sqlite3.connect(self.fs_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.label()}')
            rows = cursor.fetchall()
            names = [description[0] for description in cursor.description]
            ret = []
            for i, row in enumerate(sorted(rows)):
                row = {k: v for k, v in zip(names, row)}
                ret.append(PythonObjectPath(self, i, i, row))
        return ret


class SqliteObjectPath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            fs_path: pathlib.Path
    ):
        super().__init__(parent, position_in_parent, label, None)
        self.fs_path = fs_path

    def all_children(self) -> list[Path]:
        ret = []
        with sqlite3.connect(self.fs_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            for i, (table, ) in enumerate(sorted(tables)):
                ret.append(SqliteTablePath(self, i, table, self.fs_path))
        return ret
