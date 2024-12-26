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
    def test_must_intersect_single_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, 'true intersect true'), [True])
        self.assertEqual(evaluate(root, 'false intersect true'), [])
        self.assertEqual(evaluate(root, '5 intersect 4'), [])
        self.assertEqual(evaluate(root, '5 intersect 5'), [5])
        self.assertEqual(evaluate(root, '5 intersect 5.0'), [5])
        self.assertEqual(evaluate(root, '5 intersect "5"'), [])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type

    def test_must_intersect_single_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '5 intersect [5,1,9]'), [5])
        self.assertEqual(evaluate(root, '5 intersect [5,1,"9"]'), [5])
        self.assertEqual(evaluate(root, '5 intersect []'), [])

    def test_must_intersect_seq_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '[5,1,9] intersect 5'), [5])
        self.assertEqual(evaluate(root, '[5,1,"9"] intersect 5'), [5])
        self.assertEqual(evaluate(root, '[] intersect 5'), [])

    def test_must_intersect_seq_vs_seq(self):
        root = {}
        self.assertEqual(sorted(evaluate(root, '[5,7,9] intersect [5,1,9]')), [5, 9])
        self.assertEqual(sorted(evaluate(root, '[5,7,9] intersect [5,1,"9"]')), [5])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type
        self.assertEqual(sorted(evaluate(root, '[5,7,9] intersect []')), [])
        self.assertEqual(sorted(evaluate(root, '[] intersect [5,7,9]')), [])


if __name__ == '__main__':
    unittest.main()
