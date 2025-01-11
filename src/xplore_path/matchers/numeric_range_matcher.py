from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class NumericRangeMatcher(Matcher):
    def __init__(self, min_: float, min_inclusive: bool, max_: float, max_inclusive: bool):
        self.min_ = min_
        self.min_inclusive = min_inclusive
        self.max_ = max_
        self.max_inclusive = max_inclusive

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(float)
        if value is None:
            return False
        value = value.value
        if value is None:
            return False
        if self.min_inclusive and self.max_inclusive:
            return self.min_ <= value <= self.max_
        elif self.min_inclusive and not self.max_inclusive:
            return self.min_ <= value < self.max_
        elif not self.min_inclusive and self.max_inclusive:
            return self.min_ < value <= self.max_
        elif not self.min_inclusive and not self.max_inclusive:
            return self.min_ < value < self.max_
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