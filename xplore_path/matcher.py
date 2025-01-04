from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Hashable


class Matcher(ABC):
    @abstractmethod
    def match(self, value: Hashable) -> bool:
        ...