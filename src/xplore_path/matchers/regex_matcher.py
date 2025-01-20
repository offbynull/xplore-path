import re

from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class RegexMatcher(Matcher):
    """
    ``Matcher`` that matches using regex. If value isn't a string, it's coerced into one prior to testing for a match.
    """
    def __init__(self, pattern: str):
        """
        Construct a ``RegexMatcher`` object.
        :param pattern: Regex pattern to test against.
        :raises ValueError: If ``pattern`` isn't valid a regex pattern.
        """
        try:
            self._pattern = re.compile(pattern)
        except re.error as e:
            raise ValueError(e)

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        return bool(re.search(self._pattern, value))