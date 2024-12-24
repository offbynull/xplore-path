from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.coercions import LABEL_TYPE


class StrictLabelMatcher(LabelMatcher):
    def __init__(self, pattern: LABEL_TYPE):
        self.pattern = pattern

    def match(self, value: LABEL_TYPE) -> bool:
        return self.pattern == value