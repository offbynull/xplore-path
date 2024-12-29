from __future__ import annotations

import pathlib
from abc import ABC, abstractmethod
from typing import Any


class FileLoader(ABC):
    @abstractmethod
    def is_loadable(self, p: pathlib.Path) -> bool:
        ...

    @abstractmethod
    def load(self, p: pathlib.Path) -> Any:
        ...
