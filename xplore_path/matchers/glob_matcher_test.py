import math
import unittest

from xplore_path.matchers.glob_matcher import GlobMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertTrue(GlobMatcher('J*').match('John'))
        self.assertTrue(GlobMatcher('J*').match('Jane'))
        self.assertFalse(GlobMatcher('J*').match('Bob'))
        self.assertFalse(GlobMatcher('J*').match(None))
        self.assertFalse(GlobMatcher('J*').match(0))
        self.assertFalse(GlobMatcher('J*').match(1.0))
        self.assertFalse(GlobMatcher('J*').match(math.nan))
        self.assertFalse(GlobMatcher('J*').match(math.inf))


if __name__ == '__main__':
    unittest.main()
