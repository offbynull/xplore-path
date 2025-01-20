from xplore_path.matcher import Matcher


class WildcardMatcher(Matcher):
    """
    ``Matcher`` that matches anything.
    """
    def match(self, value: str | int | float | bool) -> bool:
        return True