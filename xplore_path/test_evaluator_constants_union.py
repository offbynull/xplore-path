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
    def test_must_union_single_vs_single(self):
        root = {}
        self.assertEqual(set(evaluate(root, 'true union true')), {True})
        self.assertEqual(set(evaluate(root, 'false union true')), {False, True})
        self.assertEqual(set(evaluate(root, '5 union 4')), {4, 5})
        self.assertEqual(set(evaluate(root, '5 union 5')), {5})
        self.assertEqual(set(evaluate(root, '5 union 5.0')), {5})
        self.assertEqual(set(evaluate(root, '5 union "5"')), {5, '5'})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type

    def test_must_union_single_vs_seq(self):
        root = {}
        self.assertEqual(set(evaluate(root, '5 union [5,1,9]')), {9, 5, 1})
        self.assertEqual(set(evaluate(root, '5 union [5,1,"9"]')), {'9', 5, 1})
        self.assertEqual(set(evaluate(root, '5 union []')), {5})

    def test_must_union_seq_vs_single(self):
        root = {}
        self.assertEqual(set(evaluate(root, '[5,1,9] union 5')), {9, 5, 1})
        self.assertEqual(set(evaluate(root, '[5,1,"9"] union 5')), {'9', 5, 1})
        self.assertEqual(set(evaluate(root, '[] union 5')), {5})

    def test_must_union_seq_vs_seq(self):
        root = {}
        self.assertEqual(set(evaluate(root, '[5,7,9] union [5,1,9]')), {9, 7, 5, 1})
        self.assertEqual(set(evaluate(root, '[5,7,9] union [5,1,"9"]')), {'9', 9, 7, 5, 1})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type
        self.assertEqual(set(evaluate(root, '[5,7,9] union []')), {5,7,9})
        self.assertEqual(set(evaluate(root, '[] union [5,7,9]')), {5,7,9})


if __name__ == '__main__':
    unittest.main()
