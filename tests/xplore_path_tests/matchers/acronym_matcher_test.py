import unittest

from xplore_path.matchers.acronym_matcher import AcronymMatcher


class TestCase(unittest.TestCase):
    def test_must_match(self):
        self.assertTrue(AcronymMatcher('hw').match('hello_world'))
        self.assertFalse(AcronymMatcher('hw').match('Hello_world'))
        self.assertFalse(AcronymMatcher('hw').match('Hello_World'))
        self.assertFalse(AcronymMatcher('hw').match('HELLOW_WORLD'))
        self.assertTrue(AcronymMatcher('hW').match('helloWorld'))
        self.assertTrue(AcronymMatcher('HW').match('HelloWorld'))
        self.assertFalse(AcronymMatcher('HW').match('HELLOWORLD'))


if __name__ == '__main__':
    unittest.main()
