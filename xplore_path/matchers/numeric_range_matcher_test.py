import math
import unittest

from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(-1))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(0))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(1))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(2))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(3))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(4))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match(4.999))
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(5))
        self.assertTrue(NumericRangeMatcher(0, True, 5, True).match(5))
        self.assertFalse(NumericRangeMatcher(0, False, 5, True).match(0))

        self.assertFalse(NumericRangeMatcher(0, False, 5, False).match(0))
        self.assertTrue(NumericRangeMatcher(0, False, 5, False).match(1))
        self.assertTrue(NumericRangeMatcher(0, False, 5, False).match(4))
        self.assertFalse(NumericRangeMatcher(0, False, 5, False).match(5))

        self.assertFalse(NumericRangeMatcher(0, True, 5, True).match(-1))
        self.assertTrue(NumericRangeMatcher(0, True, 5, True).match(0))
        self.assertTrue(NumericRangeMatcher(0, True, 5, True).match(5))
        self.assertFalse(NumericRangeMatcher(0, True, 5, True).match(6))

        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(math.nan))

        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(math.inf))
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(-math.inf))

        self.assertFalse(NumericRangeMatcher(-math.inf, False, math.inf, False).match(-math.inf))
        self.assertTrue(NumericRangeMatcher(-math.inf, False, math.inf, False).match(1))
        self.assertTrue(NumericRangeMatcher(-math.inf, False, math.inf, False).match(4))
        self.assertFalse(NumericRangeMatcher(-math.inf, False, math.inf, False).match(math.inf))

        self.assertTrue(NumericRangeMatcher(-math.inf, True, math.inf, True).match(-math.inf))
        self.assertTrue(NumericRangeMatcher(-math.inf, True, math.inf, True).match(1))
        self.assertTrue(NumericRangeMatcher(-math.inf, True, math.inf, True).match(4))
        self.assertTrue(NumericRangeMatcher(-math.inf, True, math.inf, True).match(math.inf))

        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(None))
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(''))
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match('a'))
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match('2'))  # coerced to float
        self.assertTrue(NumericRangeMatcher(0, True, 5, False).match('2.0'))  # coerced to float
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(math.nan))
        self.assertFalse(NumericRangeMatcher(0, True, 5, False).match(math.inf))


if __name__ == '__main__':
    unittest.main()
