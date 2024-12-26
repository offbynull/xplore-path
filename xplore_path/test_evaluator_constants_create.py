import math
import unittest

from xplore_path.evaluator import evaluate
from xplore_path.label_matchers.fuzzy_label_matcher import FuzzyLabelMatcher
from xplore_path.label_matchers.glob_label_matcher import GlobLabelMatcher
from xplore_path.label_matchers.regex_label_matcher import RegexLabelMatcher
from xplore_path.label_matchers.strict_label_matcher import StrictLabelMatcher
from xplore_path.label_matchers.wildcard_label_matcher import WildcardLabelMatcher
from xplore_path.raise_parse_error_listener import ParseException


class EvaluatorTest(unittest.TestCase):
    def test_must_produce_literals(self):
        root = {}
        self.assertEqual(evaluate(root, 'true'), True)
        self.assertEqual(evaluate(root, 'false'), False)
        self.assertEqual(evaluate(root, '"abc"'), 'abc')
        self.assertEqual(evaluate(root, '\'abc\''), 'abc')
        self.assertEqual(evaluate(root, 'abc'), 'abc')
        self.assertEqual(evaluate(root, '"ab""c"'), 'ab"c')
        self.assertEqual(evaluate(root, '\'ab\'\'c\''), 'ab\'c')
        self.assertEqual(evaluate(root, '123'), 123)
        self.assertEqual(evaluate(root, '123.0'), 123.0)
        self.assertEqual(evaluate(root, 'inf'), math.inf)

    def test_must_produce_matchers(self):
        root = {}
        self.assertIsInstance(evaluate(root, '*'), WildcardLabelMatcher)
        self.assertIsInstance(evaluate(root, 's"hello"'), StrictLabelMatcher)
        self.assertIsInstance(evaluate(root, 's\'hello\''), StrictLabelMatcher)
        self.assertIsInstance(evaluate(root, 'r"hello"'), RegexLabelMatcher)
        self.assertIsInstance(evaluate(root, 'r\'hello\''), RegexLabelMatcher)
        self.assertIsInstance(evaluate(root, 'f"hello"'), FuzzyLabelMatcher)
        self.assertIsInstance(evaluate(root, 'f\'hello\''), FuzzyLabelMatcher)
        self.assertIsInstance(evaluate(root, 'g"hello"'), GlobLabelMatcher)
        self.assertIsInstance(evaluate(root, 'g\'hello\''), GlobLabelMatcher)

    def test_must_wrap_literals_as_list_when_using_square_brackets(self):
        root = {}
        self.assertEqual(evaluate(root, '[]'), [])
        self.assertEqual(evaluate(root, '[a]'), ['a'])
        self.assertEqual(evaluate(root, '["a"]'), ['a'])
        self.assertEqual(evaluate(root, '[0]'), [0])
        self.assertEqual(evaluate(root, '[0.5]'), [0.5])
        self.assertEqual(evaluate(root, '[true]'), [True])
        self.assertEqual(evaluate(root, '[a,1, 2.5,true,false]'), ['a', 1, 2.5, True, False])

    def test_must_keep_literals_as_is_when_using_parenthesis(self):
        root = {}
        self.assertRaises(ParseException, evaluate, root, '()')
        self.assertEqual(evaluate(root, '(a)'), 'a')
        self.assertEqual(evaluate(root, '("a")'), 'a')
        self.assertEqual(evaluate(root, '(0)'), 0)
        self.assertEqual(evaluate(root, '(0.5)'), 0.5)
        self.assertEqual(evaluate(root, '(true)'), True)
        self.assertEqual(evaluate(root, '(a,1, 2.5,true,false)'), ['a', 1, 2.5, True, False])


if __name__ == '__main__':
    unittest.main()
