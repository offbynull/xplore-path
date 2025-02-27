import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_mod_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '30 mod 4'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '30.0 mod 4'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '30 mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '30.0 mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '30.0 mod "4"'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '"30" mod 4.0'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '"30" mod "4"'), 2.0)
        self.assertEqual(evaluate(DummyNode(), '30 mod x'), [])

    def test_must_mod_single_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '30 mod (4,6)'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '30.0 mod (4,6)'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '30 mod (4.0,6.0)'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '30.0 mod (4.0,6.0)'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '30.0 mod ("4","6")'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '"30" mod (4.0, 6.0)'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '"30" mod ("4", "6")'), [2.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '30 mod (x, 6)'), [0.0])
        self.assertEqual(evaluate(DummyNode(), '30 mod ()'), [])

    def test_must_mod_seq_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '(30,25) mod 6'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '(30,25) mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '(30.0,25.0) mod 6'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '(30.0,25.0) mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '("30","25") mod 6.0'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '(30.0, 25.0) mod "6"'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '("30", "25") mod "6"'), [0.0, 1.0])
        self.assertEqual(evaluate(DummyNode(), '(x, 25) mod 6'), [1.0])
        self.assertEqual(evaluate(DummyNode(), '() mod 6'), [])

    def test_must_mod_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '(7,8) mod (2,3)'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") mod ("2",3.0)'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") mod ("2",x)'), [1.0])
        self.assertEqual(evaluate(DummyNode(), '(7,8) mod ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() mod (1.2)'), [])

    def test_must_mod_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyNode(), '(7,8) zip mod (2,3)'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") zip mod ("2",3.0)'), [1.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") zip mod ("2",x)'), [1.0])
        self.assertEqual(evaluate(DummyNode(), '(7,8) zip mod ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() zip mod (1.2)'), [])

    def test_must_mod_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyNode(), '(7,8) product mod (2,3)'), [1.0, 1.0, 0.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") product mod ("2",3.0)'), [1.0, 1.0, 0.0, 2.0])
        self.assertEqual(evaluate(DummyNode(), '(7,"8") product mod ("2",x)'), [1.0, 0.0])
        self.assertEqual(evaluate(DummyNode(), '(7,8) product mod ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() product mod (1.2)'), [])


if __name__ == '__main__':
    unittest.main()
