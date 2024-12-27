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
    def test_must_negate_single(self):
        self.assertEqual(evaluate(DummyPath(), '-5'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-5.0'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-"5"'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-"-5"'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '-x'), [])

    def test_must_negate_seq(self):
        self.assertEqual(evaluate(DummyPath(), '-[5, 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-[5.0, 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-["5", 6]'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-["-5", 6]'), [5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-[x, 6]'), [-6.0])
        self.assertEqual(evaluate(DummyPath(), '-[x]'), [])
        self.assertEqual(evaluate(DummyPath(), '-[]'), [])


if __name__ == '__main__':
    unittest.main()
