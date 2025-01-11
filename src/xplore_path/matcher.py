from __future__ import annotations

from abc import ABC, abstractmethod


class Matcher(ABC):
    @abstractmethod
    def match(self, value: str | int | float | bool) -> bool:
        ...