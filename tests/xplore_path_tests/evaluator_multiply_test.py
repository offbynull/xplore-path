import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_multiply_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '5*5'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '5.0*5'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '5*5.0'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '5.0*5.0'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '5.0*"5"'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '"5"*5.0'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '"5"*"5"'), 25.0)
        self.assertEqual(evaluate(DummyNode(), '5*x'), [])

    def test_must_multiply_single_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '5*(5,6)'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '5.0*(5,6)'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '5*(5.0,6.0)'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '5.0*(5.0,6.0)'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '5.0*("5","6")'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '"5"*(5.0, 6.0)'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '"5"*("5", "6")'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '5*(x, 6)'), [30.0])
        self.assertEqual(evaluate(DummyNode(), '5*()'), [])

    def test_must_multiply_seq_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '(5,6)*5'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '(5,6)*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '(5.0,6.0)*5'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '(5.0,6.0)*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '("5","6")*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '(5.0, 6.0)*"5"'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '("5", "6")*"5"'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyNode(), '(x, 6)*5'), [30.0])
        self.assertEqual(evaluate(DummyNode(), '()*5'), [])

    def test_must_multiply_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2)*(3,4)'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2")*("3",4.0)'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2")*("3",x)'), [3.0])
        self.assertEqual(evaluate(DummyNode(), '(1,2)*()'), [])
        self.assertEqual(evaluate(DummyNode(), '()*(1.2)'), [])

    def test_must_multiply_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2) zip * (3,4)'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") zip * ("3",4.0)'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") zip * ("3",x)'), [3.0])
        self.assertEqual(evaluate(DummyNode(), '(1,2) zip * ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() zip * (1.2)'), [])

    def test_must_multiply_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2) product * (3,4)'), [3.0, 4.0, 6.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") product * ("3",4.0)'), [3.0, 4.0, 6.0, 8.0])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") product * ("3",x)'), [3.0, 6.0])
        self.assertEqual(evaluate(DummyNode(), '(1,2) product * ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() product * (1.2)'), [])


if __name__ == '__main__':
    unittest.main()
