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
    def test_must_add_single_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '5+5'), 10.0)
        self.assertEqual(evaluate(root, '5.0+5'), 10.0)
        self.assertEqual(evaluate(root, '5+5.0'), 10.0)
        self.assertEqual(evaluate(root, '5.0+5.0'), 10.0)
        self.assertEqual(evaluate(root, '5.0+"5"'), 10.0)
        self.assertEqual(evaluate(root, '"5"+5.0'), 10.0)
        self.assertEqual(evaluate(root, '"5"+"5"'), 10.0)
        self.assertEqual(evaluate(root, '5+x'), [])

    def test_must_add_single_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '5+[5,6]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '5.0+[5,6]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '5+[5.0,6.0]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '5.0+[5.0,6.0]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '5.0+["5","6"]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '"5"+[5.0, 6.0]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '"5"+["5", "6"]'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '5+[x, 6]'), [11.0])
        self.assertEqual(evaluate(root, '5+[]'), [])

    def test_must_add_seq_vs_single(self):
        root = {}
        self.assertEqual(evaluate(root, '[5,6]+5'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '[5,6]+5.0'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '[5.0,6.0]+5'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '[5.0,6.0]+5.0'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '["5","6"]+5.0'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '[5.0, 6.0]+"5"'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '["5", "6"]+"5"'), [10.0, 11.0])
        self.assertEqual(evaluate(root, '[x, 6]+5'), [11.0])
        self.assertEqual(evaluate(root, '[]+5'), [])

    def test_must_add_seq_vs_seq(self):
        root = {}
        self.assertEqual(evaluate(root, '[1,2]+[3,4]'), [4.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"]+["3",4.0]'), [4.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"]+["3",x]'), [4.0])
        self.assertEqual(evaluate(root, '[1,2]+[]'), [])
        self.assertEqual(evaluate(root, '[]+[1.2]'), [])

    def test_must_add_seq_vs_seq_using_zip(self):
        root = {}
        self.assertEqual(evaluate(root, '[1,2] zip + [3,4]'), [4.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"] zip + ["3",4.0]'), [4.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"] zip + ["3",x]'), [4.0])
        self.assertEqual(evaluate(root, '[1,2] zip + []'), [])
        self.assertEqual(evaluate(root, '[] zip + [1.2]'), [])

    def test_must_add_seq_vs_seq_using_product(self):
        root = {}
        self.assertEqual(evaluate(root, '[1,2] product + [3,4]'), [4.0, 5.0, 5.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"] product + ["3",4.0]'), [4.0, 5.0, 5.0, 6.0])
        self.assertEqual(evaluate(root, '[1,"2"] product + ["3",x]'), [4.0, 5.0])
        self.assertEqual(evaluate(root, '[1,2] product + []'), [])
        self.assertEqual(evaluate(root, '[] product + [1.2]'), [])


if __name__ == '__main__':
    unittest.main()
