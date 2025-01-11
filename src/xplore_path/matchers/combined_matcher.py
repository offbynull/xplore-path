from xplore_path.matcher import Matcher


class CombinedMatcher(Matcher):
    def __init__(self, inner: list[Matcher]):
        self.inner = inner

    def match(self, value: str | int | float | bool) -> bool:
        return any(m.match(value) for m in self.inner)