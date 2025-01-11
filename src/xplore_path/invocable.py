from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from xplore_path.collection import Collection


class Invocable(ABC):
    @abstractmethod
    def invoke(self, args: list[Collection]) -> Collection:
        pass