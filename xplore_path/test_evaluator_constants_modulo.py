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
    def test_must_mod_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '30 mod 4'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 mod 4'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '30 mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 mod "4"'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '"30" mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '"30" mod "4"'), 2.0)
        self.assertEqual(evaluate(DummyPath(), '30 mod x'), [])

    def test_must_mod_single_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '30 mod [4,6]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 mod [4,6]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '30 mod [4.0,6.0]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 mod [4.0,6.0]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 mod ["4","6"]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '"30" mod [4.0, 6.0]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '"30" mod ["4", "6"]'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '30 mod [x, 6]'), [0.0])
        self.assertEqual(evaluate(DummyPath(), '30 mod []'), [])

    def test_must_mod_seq_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '[30,25] mod 6'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '[30,25] mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '[30.0,25.0] mod 6'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '[30.0,25.0] mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '["30","25"] mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '[30.0, 25.0] mod "6"'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '["30", "25"] mod "6"'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyPath(), '[x, 25] mod 6'), [1.0])
        self.assertEqual(evaluate(DummyPath(), '[] mod 6'), [])

    def test_must_mod_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '[7,8] mod [2,3]'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] mod ["2",3.0]'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] mod ["2",x]'), [1.0])
        self.assertEqual(evaluate(DummyPath(), '[7,8] mod []'), [])
        self.assertEqual(evaluate(DummyPath(), '[] mod [1.2]'), [])

    def test_must_mod_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyPath(), '[7,8] zip mod [2,3]'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] zip mod ["2",3.0]'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] zip mod ["2",x]'), [1.0])
        self.assertEqual(evaluate(DummyPath(), '[7,8] zip mod []'), [])
        self.assertEqual(evaluate(DummyPath(), '[] zip mod [1.2]'), [])

    def test_must_mod_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyPath(), '[7,8] product mod [2,3]'), [1.0, 1.0, 0.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] product mod ["2",3.0]'), [1.0, 1.0, 0.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '[7,"8"] product mod ["2",x]'), [1.0, 0.0])
        self.assertEqual(evaluate(DummyPath(), '[7,8] product mod []'), [])
        self.assertEqual(evaluate(DummyPath(), '[] product mod [1.2]'), [])


if __name__ == '__main__':
    unittest.main()
