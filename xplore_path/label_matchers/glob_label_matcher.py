import fnmatch

from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.coercions import LABEL_TYPE, coerce_single_value


class GlobLabelMatcher(LabelMatcher):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        value = coerce_single_value(value, str)
        if value is None:
            return False
        return bool(fnmatch.fnmatch(value, self.pattern))