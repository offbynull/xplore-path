from xplore_path.matcher.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE


class StrictMatcher(Matcher):
    def __init__(self, pattern: LABEL_TYPE):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        return self.pattern == value