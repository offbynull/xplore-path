from __future__ import annotations

import pathlib
from abc import ABC, abstractmethod
from typing import Any, Callable

from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath

PATH_LOADER = Callable[[Path, Any, Any, Any], Path]  # path, position_in_parent, label, data


class FileLoader(ABC):
    @abstractmethod
    def is_loadable(self, p: pathlib.Path) -> bool:
        ...

    def is_cachable(self, p: pathlib.Path) -> bool:
        return True

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return PythonObjectPath

    @abstractmethod
    def load(self, p: pathlib.Path) -> Any:
        ...
