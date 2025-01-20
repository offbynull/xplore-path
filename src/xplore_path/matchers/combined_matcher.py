from xplore_path.matcher import Matcher


class CombinedMatcher(Matcher):
    """
    ``Matcher`` that's combines several ``Matcher``\s under a single umbrella (composite). When matching, inner
    ``Matcher``\s are invoked one-by-one on the value being tested. For this ``Matcher`` to report a match, at least one
    of its inner ``Matcher``\s must report a match.
    """
    def __init__(self, inner: list[Matcher]):
        """
        Construct a ``CombinedMatcher``.
        :param inner: Inner ``Matcher``\s.
        """
        self._inner = inner

    def match(self, value: str | int | float | bool) -> bool:
        return any(m.match(value) for m in self._inner)