from xplore_path.matcher import Matcher


class StrictMatcher(Matcher):
    """
    ``Matcher`` that matches strictly, meaning without coercion (types must match).
    """
    def __init__(self, pattern: str | int | float | bool):
        """
        Construct a ``StrictMatcher`` object.
        :param pattern: Value to test for.
        """
        self._pattern = pattern

    def match(self, value: str | int | float | bool) -> bool:
        if type(self._pattern) in {int, float} and type(value) in {int, float}:
            return self._pattern == value  # Special case - treat numbers as equal
        return type(value) == type(self._pattern) and self._pattern == value  # Otherwise ensure types match
        # Why is type test required? e.g. bool inherits from int