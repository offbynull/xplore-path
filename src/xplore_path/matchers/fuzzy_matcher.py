from difflib import SequenceMatcher

from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class FuzzyMatcher(Matcher):
    """
    ``Matcher`` that matches using Python's ``SequenceMatcher``, where a reported similarity of 80% of higher is
    considered a match. If value isn't a string, it's coerced into one prior to testing for a match.
    """
    def __init__(self, pattern: str):
        """
        Construct a ``FuzzyMatcher`` object.
        :param pattern: String to test against.
        """
        self._pattern = pattern

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        return SequenceMatcher(None, self._pattern, value).ratio() >= 0.8