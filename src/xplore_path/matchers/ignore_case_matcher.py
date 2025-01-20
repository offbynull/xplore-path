from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class IgnoreCaseMatcher(Matcher):
    """
    ``Matcher`` that matches with case insensitivity. If value isn't a string, it's coerced into one prior to testing
    for a match.
    """
    def __init__(self, pattern: str):
        """
        Construct a ``IgnoreCaseMatcher`` object.
        :param pattern: String to test against.
        """
        self._pattern_casefolded = pattern.casefold()

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        return value.casefold() == self._pattern_casefolded