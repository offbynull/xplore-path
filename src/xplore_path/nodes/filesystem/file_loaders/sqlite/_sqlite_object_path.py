from __future__ import annotations

import pathlib
import sqlite3

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class SqliteTableNode(Node):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            fs_path: pathlib.Path,
    ):
        super().__init__(parent, None)
        self.fs_path = fs_path

    def children(self) -> list[Node]:
        with sqlite3.connect(self.fs_path) as conn:
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM {self.label()}')
            rows = cursor.fetchall()
            names = [description[0] for description in cursor.description]
            ret = []
            for i, row in enumerate(sorted(rows)):
                row = {k: v for k, v in zip(names, row)}
                ret.append(PythonObjectNode(ParentBlock(self, i, i), row))
        return ret


class SqliteObjectNode(Node):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            fs_path: pathlib.Path
    ):
        super().__init__(parent, None)
        self.fs_path = fs_path

    def children(self) -> list[Node]:
        ret = []
        with sqlite3.connect(self.fs_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            for i, (table, ) in enumerate(sorted(tables)):
                ret.append(SqliteTableNode(ParentBlock(self, i, table), self.fs_path))
        return ret
