from typing import Hashable

from xplore_path.matcher import Matcher


class WildcardMatcher(Matcher):
    def match(self, value: Hashable) -> bool:
        return True