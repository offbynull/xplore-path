from xplore_path.matcher.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE


class WildcardMatcher(Matcher):
    def match(self, value: LABEL_TYPE) -> bool:
        return True