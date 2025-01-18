import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_intersect_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), 'true intersect true'), [True])
        self.assertEqual(evaluate(DummyNode(), 'false intersect true'), [])
        self.assertEqual(evaluate(DummyNode(), '5 intersect 4'), [])
        self.assertEqual(evaluate(DummyNode(), '5 intersect 5'), [5])
        self.assertEqual(evaluate(DummyNode(), '5 intersect 5.0'), [5])
        self.assertEqual(evaluate(DummyNode(), '5 intersect "5"'), [])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type

    def test_must_intersect_single_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '5 intersect (5,1,9)'), [5])
        self.assertEqual(evaluate(DummyNode(), '5 intersect (5,1,"9")'), [5])
        self.assertEqual(evaluate(DummyNode(), '5 intersect ()'), [])

    def test_must_intersect_seq_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '(5,1,9) intersect 5'), [5])
        self.assertEqual(evaluate(DummyNode(), '(5,1,"9") intersect 5'), [5])
        self.assertEqual(evaluate(DummyNode(), '() intersect 5'), [])

    def test_must_intersect_seq_vs_seq(self):
        self.assertEqual(sorted(evaluate(DummyNode(), '(5,7,9) intersect (5,1,9)').unpack), [5, 9])
        self.assertEqual(sorted(evaluate(DummyNode(), '(5,7,9) intersect (5,1,"9")').unpack), [5])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type
        self.assertEqual(sorted(evaluate(DummyNode(), '(5,7,9) intersect ()').unpack), [])
        self.assertEqual(sorted(evaluate(DummyNode(), '() intersect (5,7,9)').unpack), [])


if __name__ == '__main__':
    unittest.main()
