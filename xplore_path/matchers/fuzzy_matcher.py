from difflib import SequenceMatcher
from typing import Hashable

from xplore_path.coercions import coerce_single_value
from xplore_path.matcher import Matcher


class FuzzyMatcher(Matcher):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, value: Hashable) -> bool:
        value = coerce_single_value(value, str)
        if value is None:
            return False
        return SequenceMatcher(None, self.pattern, value).ratio() >= 0.8