import math
import unittest

from xplore_path.matchers.ignore_case_matcher import IgnoreCaseMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertTrue(IgnoreCaseMatcher('strawberry').match('strawberry'))
        self.assertTrue(IgnoreCaseMatcher('strawberry').match('StRaWBERRY'))
        self.assertTrue(IgnoreCaseMatcher('').match(''))
        self.assertFalse(IgnoreCaseMatcher('strawberry').match(None))
        self.assertFalse(IgnoreCaseMatcher('strawberry').match(0))
        self.assertFalse(IgnoreCaseMatcher('strawberry').match(1.0))
        self.assertFalse(IgnoreCaseMatcher('strawberry').match(math.nan))
        self.assertFalse(IgnoreCaseMatcher('strawberry').match(math.inf))


if __name__ == '__main__':
    unittest.main()
