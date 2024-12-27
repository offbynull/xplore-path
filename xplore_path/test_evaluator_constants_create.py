import math
import unittest

from paths.dummy_path import DummyPath
from xplore_path.evaluator import evaluate
from xplore_path.label_matchers.fuzzy_label_matcher import FuzzyLabelMatcher
from xplore_path.label_matchers.glob_label_matcher import GlobLabelMatcher
from xplore_path.label_matchers.regex_label_matcher import RegexLabelMatcher
from xplore_path.label_matchers.strict_label_matcher import StrictLabelMatcher
from xplore_path.label_matchers.wildcard_label_matcher import WildcardLabelMatcher
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
        self.assertIsInstance(evaluate(DummyPath(), '*'), WildcardLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 's"hello"'), StrictLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 's\'hello\''), StrictLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'r"hello"'), RegexLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'r\'hello\''), RegexLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'f"hello"'), FuzzyLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'f\'hello\''), FuzzyLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'g"hello"'), GlobLabelMatcher)
        self.assertIsInstance(evaluate(DummyPath(), 'g\'hello\''), GlobLabelMatcher)

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
