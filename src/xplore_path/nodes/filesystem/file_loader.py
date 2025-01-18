from __future__ import annotations

import pathlib
from abc import ABC, abstractmethod
from typing import Any, Callable

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode

PATH_LOADER = Callable[[ParentBlock | None, Any], Node]  # path, position_in_parent, label, data


class FileLoader(ABC):
    @abstractmethod
    def is_loadable(self, p: pathlib.Path) -> bool:
        ...

    def is_cachable(self, p: pathlib.Path) -> bool:
        return True

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return PythonObjectNode

    @abstractmethod
    def load(self, p: pathlib.Path) -> Any:
        ...
