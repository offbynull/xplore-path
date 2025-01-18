import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_concatenate_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '(true,true)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(false,true)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,4)'), [5, 4])
        self.assertEqual(evaluate(DummyNode(), '(5,5)'), [5, 5])
        self.assertEqual(evaluate(DummyNode(), '(5,5.0)'), [5, 5.0])
        self.assertEqual(evaluate(DummyNode(), '(5,"5")'), [5, '5'])

    def test_must_concatenate_single_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '(5,(5,1,9))'), [5, 5, 1, 9])
        self.assertEqual(evaluate(DummyNode(), '(5,(5,1,"9"))'), [5, 5, 1, '9'])
        self.assertEqual(evaluate(DummyNode(), '(5,())'), [5])

    def test_must_concatenate_seq_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '((5,1,9),5)'), [5, 1, 9, 5])
        self.assertEqual(evaluate(DummyNode(), '((5,1,"9"),5)'), [5, 1, '9', 5])
        self.assertEqual(evaluate(DummyNode(), '((),5)'), [5])

    def test_must_concatenate_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '((5,7,9),(5,1,9))'), [5, 7, 9, 5, 1, 9])
        self.assertEqual(evaluate(DummyNode(), '((5,7,9),(5,1,"9"))'), [5, 7, 9, 5, 1, '9'])  # THIS IS WHAT XPATH DOES - no coercing before matching - concatenates with just data and type
        self.assertEqual(evaluate(DummyNode(), '((5,7,9),())'), [5, 7, 9])
        self.assertEqual(evaluate(DummyNode(), '((),(5,7,9))'), [5, 7, 9])


if __name__ == '__main__':
    unittest.main()
