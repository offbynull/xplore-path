import math
import unittest

from xplore_path.matchers.wildcard_matcher import WildcardMatcher


class TestCase(unittest.TestCase):
    def test_must_match_anything(self):
        m = WildcardMatcher()
        self.assertTrue(m.match(''))
        self.assertTrue(m.match('a'))
        self.assertTrue(m.match('fffff'))
        self.assertTrue(m.match(0))
        self.assertTrue(m.match(1))
        self.assertTrue(m.match(True))
        self.assertTrue(m.match(False))
        self.assertTrue(m.match(math.inf))
        self.assertTrue(m.match(-math.inf))
        self.assertTrue(m.match(math.nan))


if __name__ == '__main__':
    unittest.main()
