import math
import unittest

from xplore_path.matchers.ignore_case_label_matcher import IgnoreCaseMatcher
from xplore_path.matchers.numeric_range_label_matcher import NumericRangeMatcher
from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate
from xplore_path.matchers.fuzzy_label_matcher import FuzzyMatcher
from xplore_path.matchers.glob_label_matcher import GlobMatcher
from xplore_path.matchers.regex_label_matcher import RegexMatcher
from xplore_path.matchers.strict_label_matcher import StrictMatcher
from xplore_path.matchers.wildcard_label_matcher import WildcardMatcher
from xplore_path.raise_parse_error_listener import ParseException


class EvaluatorTest(unittest.TestCase):
    def test_must_produce_literals(self):
        self.assertEqual(evaluate(DummyPath(), 'true'), True)
        self.assertEqual(evaluate(DummyPath(), 'false'), False)
        self.assertEqual(evaluate(DummyPath(), '"abc"'), 'abc')
        self.assertEqual(evaluate(DummyPath(), '\'abc\''), 'abc')
        self.assertEqual(evaluate(DummyPath(), 'abc'), 'abc')
        self.assertEqual(evaluate(DummyPath(), '"ab""c"'), 'ab"c')
        self.assertEqual(evaluate(DummyPath(), '\'ab\'\'c\''), 'ab\'c')
        self.assertEqual(evaluate(DummyPath(), '123'), 123)
        self.assertEqual(evaluate(DummyPath(), '123.0'), 123.0)
        self.assertEqual(evaluate(DummyPath(), 'inf'), math.inf)

    def test_must_produce_matchers(self):
        self.assertIsInstance(evaluate(DummyPath(), '*'), WildcardMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 's"hello"'), StrictMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 's\'hello\''), StrictMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'r"hello"'), RegexMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'r\'hello\''), RegexMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'f"hello"'), FuzzyMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'f\'hello\''), FuzzyMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'g"hello"'), GlobMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'g\'hello\''), GlobMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'i"hello"'), IgnoreCaseMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'i\'hello\''), IgnoreCaseMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~1:5'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~[1:5]'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~[1:5)'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~(1:5]'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~(1:5)'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~1'), NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyPath(), '~1@0.001'), NumericRangeMatcher)

    def test_must_wrap_literals_as_list_when_using_square_brackets(self):
        self.assertEqual(evaluate(DummyPath(), '[]'), [])
        self.assertEqual(evaluate(DummyPath(), '[a]'), ['a'])
        self.assertEqual(evaluate(DummyPath(), '["a"]'), ['a'])
        self.assertEqual(evaluate(DummyPath(), '[0]'), [0])
        self.assertEqual(evaluate(DummyPath(), '[0.5]'), [0.5])
        self.assertEqual(evaluate(DummyPath(), '[true]'), [True])
        self.assertEqual(evaluate(DummyPath(), '[a,1, 2.5,true,false]'), ['a', 1, 2.5, True, False])

    def test_must_keep_literals_as_is_when_using_parenthesis(self):
        self.assertRaises(ParseException, evaluate, DummyPath(), '()')
        self.assertEqual(evaluate(DummyPath(), '(a)'), 'a')
        self.assertEqual(evaluate(DummyPath(), '("a")'), 'a')
        self.assertEqual(evaluate(DummyPath(), '(0)'), 0)
        self.assertEqual(evaluate(DummyPath(), '(0.5)'), 0.5)
        self.assertEqual(evaluate(DummyPath(), '(true)'), True)
        self.assertEqual(evaluate(DummyPath(), '(a,1, 2.5,true,false)'), ['a', 1, 2.5, True, False])


if __name__ == '__main__':
    unittest.main()
