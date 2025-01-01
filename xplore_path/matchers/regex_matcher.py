import re

from xplore_path.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE, coerce_single_value


class RegexMatcher(Matcher):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        value = coerce_single_value(value, str)
        if value is None:
            return False
        return bool(re.search(self.pattern, value))