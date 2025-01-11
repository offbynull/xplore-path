from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from xplore_path.entity import Entity


class FallbackMode(ABC):
    @abstractmethod
    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        ...
