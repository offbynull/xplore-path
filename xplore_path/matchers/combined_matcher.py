from xplore_path.matcher import Matcher
from xplore_path.coercions import LABEL_TYPE


class CombinedMatcher(Matcher):
    def __init__(self, inner: list[Matcher]):
        self.inner = inner

    def match(self, value: LABEL_TYPE) -> bool:
        return any(m.match(value) for m in self.inner)