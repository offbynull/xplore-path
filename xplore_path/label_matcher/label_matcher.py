from __future__ import annotations

from abc import ABC, abstractmethod
from xplore_path.coercions import LABEL_TYPE


class LabelMatcher(ABC):
    @abstractmethod
    def match(self, value: LABEL_TYPE) -> bool:
        ...