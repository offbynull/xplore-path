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
    def test_must_negate_single(self):
        root = {}
        self.assertEqual(evaluate(root, '-5'), -5.0)
        self.assertEqual(evaluate(root, '-5.0'), -5.0)
        self.assertEqual(evaluate(root, '-"5"'), -5.0)
        self.assertEqual(evaluate(root, '-"-5"'), 5.0)
        self.assertEqual(evaluate(root, '-x'), [])

    def test_must_negate_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '-[5, 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(root, '-[5.0, 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(root, '-["5", 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(root, '-["-5", 6]'), [5.0, -6.0])
        self.assertEqual(evaluate(root, '-[x, 6]'), [-6.0])
        self.assertEqual(evaluate(root, '-[x]'), [])
        self.assertEqual(evaluate(root, '-[]'), [])


if __name__ == '__main__':
    unittest.main()
