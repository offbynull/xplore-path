import math
import unittest

from xplore_path.matchers.regex_matcher import RegexMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertTrue(RegexMatcher('J.*').match('John'))
        self.assertTrue(RegexMatcher('J.*').match('Jane'))
        self.assertFalse(RegexMatcher('J.*').match('Bob'))
        self.assertFalse(RegexMatcher('J.*').match(None))
        self.assertFalse(RegexMatcher('J.*').match(0))
        self.assertFalse(RegexMatcher('J.*').match(1.0))
        self.assertFalse(RegexMatcher('J.*').match(math.nan))
        self.assertFalse(RegexMatcher('J.*').match(math.inf))


if __name__ == '__main__':
    unittest.main()
