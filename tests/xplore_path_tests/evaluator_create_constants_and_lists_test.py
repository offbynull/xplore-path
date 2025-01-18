import math
import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.matchers.fuzzy_matcher import FuzzyMatcher
from xplore_path.matchers.glob_matcher import GlobMatcher
from xplore_path.matchers.ignore_case_matcher import IgnoreCaseMatcher
from xplore_path.matchers.numeric_range_matcher import NumericRangeMatcher
from xplore_path.matchers.regex_matcher import RegexMatcher
from xplore_path.matchers.strict_matcher import StrictMatcher
from xplore_path.matchers.wildcard_matcher import WildcardMatcher
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_produce_literals(self):
        self.assertEqual(evaluate(DummyNode(), 'true'), True)
        self.assertEqual(evaluate(DummyNode(), 'false'), False)
        self.assertEqual(evaluate(DummyNode(), '"abc"'), 'abc')
        self.assertEqual(evaluate(DummyNode(), '\'abc\''), 'abc')
        self.assertEqual(evaluate(DummyNode(), 'abc'), 'abc')
        self.assertEqual(evaluate(DummyNode(), '"ab""c"'), 'ab"c')
        self.assertEqual(evaluate(DummyNode(), '\'ab\'\'c\''), 'ab\'c')
        self.assertEqual(evaluate(DummyNode(), '123'), 123)
        self.assertEqual(evaluate(DummyNode(), '123.0'), 123.0)
        self.assertEqual(evaluate(DummyNode(), 'inf'), math.inf)

    def test_must_produce_matchers(self):
        self.assertIsInstance(evaluate(DummyNode(), '*').single.value, WildcardMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 's"hello"').single.value, StrictMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 's\'hello\'').single.value, StrictMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'r"hello"').single.value, RegexMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'r\'hello\'').single.value, RegexMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'f"hello"').single.value, FuzzyMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'f\'hello\'').single.value, FuzzyMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'g"hello"').single.value, GlobMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'g\'hello\'').single.value, GlobMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'i"hello"').single.value, IgnoreCaseMatcher)
        self.assertIsInstance(evaluate(DummyNode(), 'i\'hello\'').single.value, IgnoreCaseMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~1:5').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~[1:5]').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~[1:5)').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~(1:5]').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~(1:5)').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~1').single.value, NumericRangeMatcher)
        self.assertIsInstance(evaluate(DummyNode(), '~1@0.001').single.value, NumericRangeMatcher)

    def test_must_wrap_literals_as_list(self):
        self.assertEqual(evaluate(DummyNode(), '()'), [])
        self.assertEqual(evaluate(DummyNode(), '(a,)'), ['a'])
        self.assertEqual(evaluate(DummyNode(), '("a",)'), ['a'])
        self.assertEqual(evaluate(DummyNode(), '(0,)'), [0])
        self.assertEqual(evaluate(DummyNode(), '(0.5,)'), [0.5])
        self.assertEqual(evaluate(DummyNode(), '(true,)'), [True])
        self.assertEqual(evaluate(DummyNode(), '(a,1, 2.5,true,false)'), ['a', 1, 2.5, True, False])

    def test_must_wrap_literals_as_is(self):
        self.assertEqual(evaluate(DummyNode(), '(a)'), 'a')
        self.assertEqual(evaluate(DummyNode(), '("a")'), 'a')
        self.assertEqual(evaluate(DummyNode(), '(0)'), 0)
        self.assertEqual(evaluate(DummyNode(), '(0.5)'), 0.5)
        self.assertEqual(evaluate(DummyNode(), '(true)'), True)
        self.assertEqual(evaluate(DummyNode(), '(a,1, 2.5,true,false)'), ['a', 1, 2.5, True, False])


if __name__ == '__main__':
    unittest.main()
