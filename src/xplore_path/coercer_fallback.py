from abc import ABC
from typing import Any


class CoercerFallback(ABC):
    def coerce(self, value: list[Any]) -> list[Any]:
        ...