import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_union_single_vs_single(self):
        self.assertEqual(set(evaluate(DummyNode(), 'true union true').unpack), {True})
        self.assertEqual(set(evaluate(DummyNode(), 'false union true').unpack), {False, True})
        self.assertEqual(set(evaluate(DummyNode(), '5 union 4').unpack), {4, 5})
        self.assertEqual(set(evaluate(DummyNode(), '5 union 5').unpack), {5})
        self.assertEqual(set(evaluate(DummyNode(), '5 union 5.0').unpack), {5})
        self.assertEqual(set(evaluate(DummyNode(), '5 union "5"').unpack), {5, '5'})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type

    def test_must_union_single_vs_seq(self):
        self.assertEqual(set(evaluate(DummyNode(), '5 union (5,1,9)').unpack), {9, 5, 1})
        self.assertEqual(set(evaluate(DummyNode(), '5 union (5,1,"9")').unpack), {'9', 5, 1})
        self.assertEqual(set(evaluate(DummyNode(), '5 union ()').unpack), {5})

    def test_must_union_seq_vs_single(self):
        self.assertEqual(set(evaluate(DummyNode(), '(5,1,9) union 5').unpack), {9, 5, 1})
        self.assertEqual(set(evaluate(DummyNode(), '(5,1,"9") union 5').unpack), {'9', 5, 1})
        self.assertEqual(set(evaluate(DummyNode(), '() union 5').unpack), {5})

    def test_must_union_seq_vs_seq(self):
        self.assertEqual(set(evaluate(DummyNode(), '(5,7,9) union (5,1,9)').unpack), {9, 7, 5, 1})
        self.assertEqual(set(evaluate(DummyNode(), '(5,7,9) union (5,1,"9")').unpack), {'9', 9, 7, 5, 1})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type
        self.assertEqual(set(evaluate(DummyNode(), '(5,7,9) union ()').unpack), {5, 7, 9})
        self.assertEqual(set(evaluate(DummyNode(), '() union (5,7,9)').unpack), {5, 7, 9})


if __name__ == '__main__':
    unittest.main()
