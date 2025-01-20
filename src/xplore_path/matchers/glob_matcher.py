import fnmatch

from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class GlobMatcher(Matcher):
    """
    ``Matcher`` that matches using globs. If value isn't a string, it's coerced into one prior to testing for a match.
    """
    def __init__(self, pattern: str):
        """
        Construct a ``GlobMatcher`` object.
        :param pattern: Glob pattern to test against.
        """
        self._pattern = pattern

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        return bool(fnmatch.fnmatch(value, self._pattern))