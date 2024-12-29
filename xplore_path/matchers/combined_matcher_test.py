import math
import unittest

from xplore_path.matchers.combined_matcher import CombinedMatcher
from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher
from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        m = CombinedMatcher([
            StrictMatcher(5),
            NumericRangeMatcher(0, False, 4, False),
            NumericRangeMatcher(6, False, 10, False)
        ])
        self.assertFalse(m.match(0))
        self.assertTrue(m.match(1))
        self.assertTrue(m.match(2))
        self.assertTrue(m.match(3))
        self.assertFalse(m.match(4))
        self.assertTrue(m.match(5))
        self.assertFalse(m.match(6))
        self.assertTrue(m.match(7))
        self.assertTrue(m.match(8))
        self.assertTrue(m.match(9))
        self.assertFalse(m.match(10))
        self.assertFalse(m.match(None))
        self.assertFalse(m.match(''))
        self.assertFalse(m.match('a'))
        self.assertTrue(m.match('1'))  # numeric matcher coerces to float
        self.assertTrue(m.match('1.0'))  # numeric matcher coerces to float
        self.assertFalse(m.match(math.nan))
        self.assertFalse(m.match(math.inf))


if __name__ == '__main__':
    unittest.main()
