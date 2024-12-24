from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.coercions import LABEL_TYPE


class CombinedLabelMatcher(LabelMatcher):
    def __init__(self, inner: list[LabelMatcher]):
        self.inner = inner

    def match(self, value: LABEL_TYPE) -> bool:
        return any(m.match(value) for m in self.inner)