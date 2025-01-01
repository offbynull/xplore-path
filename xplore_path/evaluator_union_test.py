import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_union_single_vs_single(self):
        self.assertEqual(set(evaluate(DummyPath(), 'true union true')), {True})
        self.assertEqual(set(evaluate(DummyPath(), 'false union true')), {False, True})
        self.assertEqual(set(evaluate(DummyPath(), '5 union 4')), {4, 5})
        self.assertEqual(set(evaluate(DummyPath(), '5 union 5')), {5})
        self.assertEqual(set(evaluate(DummyPath(), '5 union 5.0')), {5})
        self.assertEqual(set(evaluate(DummyPath(), '5 union "5"')), {5, '5'})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type

    def test_must_union_single_vs_seq(self):
        self.assertEqual(set(evaluate(DummyPath(), '5 union {5,1,9}')), {9, 5, 1})
        self.assertEqual(set(evaluate(DummyPath(), '5 union {5,1,"9"}')), {'9', 5, 1})
        self.assertEqual(set(evaluate(DummyPath(), '5 union {}')), {5})

    def test_must_union_seq_vs_single(self):
        self.assertEqual(set(evaluate(DummyPath(), '{5,1,9} union 5')), {9, 5, 1})
        self.assertEqual(set(evaluate(DummyPath(), '{5,1,"9"} union 5')), {'9', 5, 1})
        self.assertEqual(set(evaluate(DummyPath(), '{} union 5')), {5})

    def test_must_union_seq_vs_seq(self):
        self.assertEqual(set(evaluate(DummyPath(), '{5,7,9} union {5,1,9}')), {9, 7, 5, 1})
        self.assertEqual(set(evaluate(DummyPath(), '{5,7,9} union {5,1,"9"}')), {'9', 9, 7, 5, 1})  # THIS IS WHAT XPATH DOES - no coercing before matching - unions with just data and type
        self.assertEqual(set(evaluate(DummyPath(), '{5,7,9} union {}')), {5, 7, 9})
        self.assertEqual(set(evaluate(DummyPath(), '{} union {5,7,9}')), {5, 7, 9})


if __name__ == '__main__':
    unittest.main()
