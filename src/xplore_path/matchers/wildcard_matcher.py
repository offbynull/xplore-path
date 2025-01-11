from xplore_path.matcher import Matcher


class WildcardMatcher(Matcher):
    def match(self, value: str | int | float | bool) -> bool:
        return True