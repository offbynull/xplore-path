from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.coercions import LABEL_TYPE


class WildcardLabelMatcher(LabelMatcher):
    def match(self, value: LABEL_TYPE) -> bool:
        return True