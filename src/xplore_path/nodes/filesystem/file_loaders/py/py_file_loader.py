from __future__ import annotations

import pathlib
from typing import Any

from xplore_path.nodes.filesystem.file_loader import FileLoader, NODE_CREATOR
from xplore_path.nodes.mirror.mirror_node import MirrorNode
from xplore_path.nodes.python_ast.python_ast_node import PythonAstNode


class PyFileLoader(FileLoader):
    """
    ``FileLoader`` for Python files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.py'

    def node_creator(self, p: pathlib.Path) -> NODE_CREATOR:
        def creator(p, code):
            n = PythonAstNode.create_root_path(code)
            return MirrorNode(n, p)

        return creator

    def load(self, p: pathlib.Path) -> Any:
        return p.read_text()
