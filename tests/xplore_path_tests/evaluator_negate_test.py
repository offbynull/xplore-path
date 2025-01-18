import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_negate_single(self):
        self.assertEqual(evaluate(DummyNode(), '-5'), -5.0)
        self.assertEqual(evaluate(DummyNode(), '-5.0'), -5.0)
        self.assertEqual(evaluate(DummyNode(), '-"5"'), -5.0)
        self.assertEqual(evaluate(DummyNode(), '-"-5"'), 5.0)
        self.assertEqual(evaluate(DummyNode(), '-x'), [])

    def test_must_negate_seq(self):
        self.assertEqual(evaluate(DummyNode(), '-(5, 6)'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyNode(), '-(5.0, 6)'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyNode(), '-("5", 6)'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyNode(), '-("-5", 6)'), [5.0, -6.0])
        self.assertEqual(evaluate(DummyNode(), '-(x, 6)'), [-6.0])
        self.assertEqual(evaluate(DummyNode(), '-(x)'), [])
        self.assertEqual(evaluate(DummyNode(), '-()'), [])


if __name__ == '__main__':
    unittest.main()
