from difflib import SequenceMatcher

from xplore_path.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE, coerce_single_value


class FuzzyMatcher(Matcher):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        value = coerce_single_value(value, str)
        if value is None:
            return False
        return SequenceMatcher(None, self.pattern, value).ratio() >= 0.8