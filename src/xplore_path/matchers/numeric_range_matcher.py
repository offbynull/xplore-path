from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class NumericRangeMatcher(Matcher):
    """
    ``Matcher`` that tests to see if a value is within some numeric range. If value isn't a float, it's coerced into one
     prior to testing for a match.
    """
    def __init__(self, min_: float, min_inclusive: bool, max_: float, max_inclusive: bool):
        """
        Construct a ``NumericRangeMatcher``.

        :param min_: Range minimum.
        :param min_inclusive: If ``True``, ``min_`` is inclusive. Otherwise, ``min_`` is exclusive.
        :param max_: Range maximum.
        :param max_inclusive: If ``True``, ``max_`` is inclusive. Otherwise, ``max_`` is exclusive.
        """
        self._min_ = min_
        self._min_inclusive = min_inclusive
        self._max_ = max_
        self._max_inclusive = max_inclusive

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(float)
        if value is None:
            return False
        value = value.value
        if value is None:
            return False
        if self._min_inclusive and self._max_inclusive:
            return self._min_ <= value <= self._max_
        elif self._min_inclusive and not self._max_inclusive:
            return self._min_ <= value < self._max_
        elif not self._min_inclusive and self._max_inclusive:
            return self._min_ < value <= self._max_
        elif not self._min_inclusive and not self._max_inclusive:
            return self._min_ < value < self._max_
        raise ValueError('Should never reach this point')


if __name__ == '__main__':
    print(f'{NumericRangeMatcher(5, True, 7, True).match(5)=}')
    print(f'{NumericRangeMatcher(5, False, 7, True).match(5)=}')
    print(f'{NumericRangeMatcher(5, False, 7, True).match(7)=}')
    print(f'{NumericRangeMatcher(5, False, 7, False).match(7)=}')
    print(f'{NumericRangeMatcher(5, False, 7, False).match(6)=}')
    print(f'{NumericRangeMatcher(5, False, 7, True).match(6)=}')
    print(f'{NumericRangeMatcher(5, True, 7, False).match(6)=}')
    print(f'{NumericRangeMatcher(5, True, 7, True).match(6)=}')