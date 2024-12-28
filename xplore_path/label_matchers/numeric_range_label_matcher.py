import re

from xplore_path.label_matcher.label_matcher import LabelMatcher
from xplore_path.coercions import LABEL_TYPE, coerce_single_value


class NumericRangeLabelMatcher(LabelMatcher):
    def __init__(self, min_: float, min_inclusive: bool, max_: float, max_inclusive: bool):
        self.min_ = min_
        self.min_inclusive = min_inclusive
        self.max_ = max_
        self.max_inclusive = max_inclusive

    def match(self, value: LABEL_TYPE) -> bool:
        value = coerce_single_value(value, float)
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
    print(f'{NumericRangeLabelMatcher(5, True, 7, True).match(5)=}')
    print(f'{NumericRangeLabelMatcher(5, False, 7, True).match(5)=}')
    print(f'{NumericRangeLabelMatcher(5, False, 7, True).match(7)=}')
    print(f'{NumericRangeLabelMatcher(5, False, 7, False).match(7)=}')
    print(f'{NumericRangeLabelMatcher(5, False, 7, False).match(6)=}')
    print(f'{NumericRangeLabelMatcher(5, False, 7, True).match(6)=}')
    print(f'{NumericRangeLabelMatcher(5, True, 7, False).match(6)=}')
    print(f'{NumericRangeLabelMatcher(5, True, 7, True).match(6)=}')