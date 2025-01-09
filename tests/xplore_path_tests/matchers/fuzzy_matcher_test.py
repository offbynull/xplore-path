import math
import unittest

from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertTrue(FuzzyMatcher('strawberry').match('strawberry'))
        self.assertTrue(FuzzyMatcher('strawberry').match('strawbery'))
        self.assertTrue(FuzzyMatcher('strawberry').match('strbwbery'))
        self.assertFalse(FuzzyMatcher('strawberry').match('szrbwbery'))
        self.assertFalse(FuzzyMatcher('strawberry').match(None))
        self.assertFalse(FuzzyMatcher('strawberry').match(0))
        self.assertFalse(FuzzyMatcher('strawberry').match(1.0))
        self.assertFalse(FuzzyMatcher('strawberry').match(math.nan))
        self.assertFalse(FuzzyMatcher('strawberry').match(math.inf))


if __name__ == '__main__':
    unittest.main()
