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
    def test_must_divide_single_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '25 div 5'), 5.0)
        self.assertEqual(evaluate(root, '25.0 div 5'), 5.0)
        self.assertEqual(evaluate(root, '25 div 5.0'), 5.0)
        self.assertEqual(evaluate(root, '25.0 div 5.0'), 5.0)
        self.assertEqual(evaluate(root, '25.0 div "5"'), 5.0)
        self.assertEqual(evaluate(root, '"25" div 5.0'), 5.0)
        self.assertEqual(evaluate(root, '"25" div "5"'), 5.0)
        self.assertEqual(evaluate(root, '25 div x'), [])

    def test_must_divide_single_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '30 div [5,6]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 div [5,6]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '30 div [5.0,6.0]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 div [5.0,6.0]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 div ["5","6"]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '"30" div [5.0, 6.0]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '"30" div ["5", "6"]'), [6.0, 5.0])
        self.assertEqual(evaluate(root, '30 div [x, 6]'), [5.0])
        self.assertEqual(evaluate(root, '30 div []'), [])

    def test_must_divide_seq_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '[25,30] div 5'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '[25,30] div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '[25.0,30.0] div 5'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '[25.0,30.0] div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '["25","30"] div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '[25.0, 30.0] div "5"'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '["25", "30"] div "5"'), [5.0, 6.0])
        self.assertEqual(evaluate(root, '[x, 30] div 5'), [6.0])
        self.assertEqual(evaluate(root, '[] div 5'), [])

    def test_must_divide_seq_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '[6,8] div [2,4]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] div ["2",4.0]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] div ["2",x]'), [3.0])
        self.assertEqual(evaluate(root, '[6,8] div []'), [])
        self.assertEqual(evaluate(root, '[] div [1.2]'), [])

    def test_must_divide_seq_vs_seq_using_zip(self):
        root = {}
        self.assertEqual(evaluate(root, '[6,8] zip div [2,4]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] zip div ["2",4.0]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] zip div ["2",x]'), [3.0])
        self.assertEqual(evaluate(root, '[6,8] zip div []'), [])
        self.assertEqual(evaluate(root, '[] zip div [1.2]'), [])

    def test_must_divide_seq_vs_seq_using_product(self):
        root = {}
        self.assertEqual(evaluate(root, '[6,8] product div [2,4]'), [3.0, 1.5, 4.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] product div ["2",4.0]'), [3.0, 1.5, 4.0, 2.0])
        self.assertEqual(evaluate(root, '[6,"8"] product div ["2",x]'), [3.0, 4.0])
        self.assertEqual(evaluate(root, '[6,8] product div []'), [])
        self.assertEqual(evaluate(root, '[] product div [1.2]'), [])


if __name__ == '__main__':
    unittest.main()
