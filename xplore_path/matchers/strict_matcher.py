from xplore_path.matcher.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE


class StrictMatcher(Matcher):
    def __init__(self, pattern: LABEL_TYPE):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        if type(self.pattern) in {int, float} and type(value) in {int, float}:
            return self.pattern == value  # special case - treat numbers as equal
        return type(value) == type(self.pattern) and self.pattern == value  # otherwise ensure types match
        # why is type test required? e.g. bool inherits from int