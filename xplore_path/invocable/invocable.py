from abc import ABC, abstractmethod
from typing import Any


class Invocable(ABC):
    @abstractmethod
    def invoke(self, args: list[Any]) -> Any:
        pass