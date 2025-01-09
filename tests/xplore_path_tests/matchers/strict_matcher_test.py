import math
import unittest

from xplore_path.matchers.strict_matcher import StrictMatcher


class TestCase(unittest.TestCase):
    def test_must_match_using_equality_operator(self):
        self.assertTrue(StrictMatcher('').match(''))
        self.assertFalse(StrictMatcher('').match(None))
        self.assertFalse(StrictMatcher('').match(False))
        self.assertFalse(StrictMatcher('').match(True))
        self.assertFalse(StrictMatcher('').match(0))

        self.assertTrue(StrictMatcher('a').match('a'))
        self.assertFalse(StrictMatcher('a').match('b'))
        self.assertFalse(StrictMatcher('a').match(0))
        self.assertFalse(StrictMatcher('a').match(1))
        self.assertFalse(StrictMatcher('a').match(1.0))
        self.assertFalse(StrictMatcher('a').match(None))

        self.assertTrue(StrictMatcher(1).match(1))
        self.assertTrue(StrictMatcher(1).match(1.0))
        self.assertFalse(StrictMatcher(1).match(0))
        self.assertFalse(StrictMatcher(1).match('1'))
        self.assertFalse(StrictMatcher(1).match(True))
        self.assertFalse(StrictMatcher(1).match(None))

        self.assertFalse(StrictMatcher(math.nan).match(math.nan))  # nan == nan is false
        self.assertFalse(StrictMatcher(math.nan).match(math.inf))
        self.assertFalse(StrictMatcher(math.nan).match(0))
        self.assertFalse(StrictMatcher(math.nan).match('inf'))
        self.assertFalse(StrictMatcher(math.nan).match(None))

        self.assertTrue(StrictMatcher(True).match(True))
        self.assertFalse(StrictMatcher(True).match("True"))
        self.assertFalse(StrictMatcher(True).match(1))
        self.assertFalse(StrictMatcher(True).match(0))
        self.assertFalse(StrictMatcher(True).match(None))

        self.assertTrue(StrictMatcher(False).match(False))
        self.assertFalse(StrictMatcher(False).match("False"))
        self.assertFalse(StrictMatcher(False).match(1))
        self.assertFalse(StrictMatcher(False).match(0))
        self.assertFalse(StrictMatcher(False).match(None))

        self.assertTrue(StrictMatcher(1.0).match(1.0))
        self.assertTrue(StrictMatcher(1.0).match(1))
        self.assertFalse(StrictMatcher(1.0).match('1'))
        self.assertFalse(StrictMatcher(1.0).match('1.0'))
        self.assertFalse(StrictMatcher(1.0).match(True))
        self.assertFalse(StrictMatcher(1.0).match(False))
        self.assertFalse(StrictMatcher(1.0).match(None))

        self.assertTrue(StrictMatcher(None).match(None))
        self.assertFalse(StrictMatcher(None).match(0))
        self.assertFalse(StrictMatcher(None).match(math.nan))


if __name__ == '__main__':
    unittest.main()
