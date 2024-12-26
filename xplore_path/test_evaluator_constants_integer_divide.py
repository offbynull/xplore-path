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
    def test_must_integer_divide_single_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '30 idiv 4'), 7.0)
        self.assertEqual(evaluate(root, '30.0 idiv 4'), 7.0)
        self.assertEqual(evaluate(root, '30 idiv 4.0'), 7.0)
        self.assertEqual(evaluate(root, '30.0 idiv 4.0'), 7.0)
        self.assertEqual(evaluate(root, '30.0 idiv "4"'), 7.0)
        self.assertEqual(evaluate(root, '"30" idiv 4.0'), 7.0)
        self.assertEqual(evaluate(root, '"30" idiv "4"'), 7.0)
        self.assertEqual(evaluate(root, '30 idiv x'), [])

    def test_must_integer_divide_single_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '30 idiv [4,6]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 idiv [4,6]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '30 idiv [4.0,6.0]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 idiv [4.0,6.0]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '30.0 idiv ["4","6"]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '"30" idiv [4.0, 6.0]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '"30" idiv ["4", "6"]'), [7.0, 5.0])
        self.assertEqual(evaluate(root, '30 idiv [x, 6]'), [5.0])
        self.assertEqual(evaluate(root, '30 idiv []'), [])

    def test_must_integer_divide_seq_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '[30,25] idiv 6'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '[30,25] idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '[30.0,25.0] idiv 6'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '[30.0,25.0] idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '["30","25"] idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '[30.0, 25.0] idiv "6"'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '["30", "25"] idiv "6"'), [5.0, 4.0])
        self.assertEqual(evaluate(root, '[x, 25] idiv 6'), [4.0])
        self.assertEqual(evaluate(root, '[] idiv 6'), [])

    def test_must_integer_divide_seq_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '[7,8] idiv [2,3]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] idiv ["2",3.0]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] idiv ["2",x]'), [3.0])
        self.assertEqual(evaluate(root, '[7,8] idiv []'), [])
        self.assertEqual(evaluate(root, '[] idiv [1.2]'), [])

    def test_must_integer_divide_seq_vs_seq_using_zip(self):
        root = {}
        self.assertEqual(evaluate(root, '[7,8] zip idiv [2,3]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] zip idiv ["2",3.0]'), [3.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] zip idiv ["2",x]'), [3.0])
        self.assertEqual(evaluate(root, '[7,8] zip idiv []'), [])
        self.assertEqual(evaluate(root, '[] zip idiv [1.2]'), [])

    def test_must_integer_divide_seq_vs_seq_using_product(self):
        root = {}
        self.assertEqual(evaluate(root, '[7,8] product idiv [2,3]'), [3.0, 2.0, 4.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] product idiv ["2",3.0]'), [3.0, 2.0, 4.0, 2.0])
        self.assertEqual(evaluate(root, '[7,"8"] product idiv ["2",x]'), [3.0, 4.0])
        self.assertEqual(evaluate(root, '[7,8] product idiv []'), [])
        self.assertEqual(evaluate(root, '[] product idiv [1.2]'), [])


if __name__ == '__main__':
    unittest.main()
