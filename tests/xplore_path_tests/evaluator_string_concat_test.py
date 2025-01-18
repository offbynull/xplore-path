import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_concat_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '5||5'), '55')
        self.assertEqual(evaluate(DummyNode(), '5.0||5'), '55')
        self.assertEqual(evaluate(DummyNode(), '5||5.0'), '55')
        self.assertEqual(evaluate(DummyNode(), '5.0||5.0'), '55')
        self.assertEqual(evaluate(DummyNode(), '5.0||"5"'), '55')
        self.assertEqual(evaluate(DummyNode(), '"5"||5.0'), '55')
        self.assertEqual(evaluate(DummyNode(), '"5"||"5"'), '55')
        self.assertEqual(evaluate(DummyNode(), '5||x'), '5x')

    def test_must_concat_single_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '5||(5,6)'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '5.0||(5,6)'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '5||(5.0,6.0)'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '5.0||(5.0,6.0)'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '5.0||("5","6")'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '"5"||(5.0, 6.0)'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '"5"||("5", "6")'), ['55', '56'])
        self.assertEqual(evaluate(DummyNode(), '5||(x, 6)'), ['5x', '56'])
        self.assertEqual(evaluate(DummyNode(), '5||()'), [])

    def test_must_concat_seq_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '(5,6)||5'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '(5,6)||5.0'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '(5.0,6.0)||5'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '(5.0,6.0)||5.0'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '("5","6")||5.0'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '(5.0, 6.0)||"5"'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '("5", "6")||"5"'), ['55', '65'])
        self.assertEqual(evaluate(DummyNode(), '(x, 6)||5'), ['x5', '65'])
        self.assertEqual(evaluate(DummyNode(), '()||5'), [])

    def test_must_concat_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2)||(3,4)'), ['13', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2")||("3",4.0)'), ['13', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2")||("3",x)'), ['13', '2x'])
        self.assertEqual(evaluate(DummyNode(), '(1,2)||()'), [])
        self.assertEqual(evaluate(DummyNode(), '()||(1.2)'), [])

    def test_must_concat_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2) zip || (3,4)'), ['13', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") zip || ("3",4.0)'), ['13', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") zip || ("3",x)'), ['13', '2x'])
        self.assertEqual(evaluate(DummyNode(), '(1,2) zip || ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() zip || (1.2)'), [])

    def test_must_concat_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyNode(), '(1,2) product || (3,4)'), ['13', '14', '23', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") product || ("3",4.0)'), ['13', '14', '23', '24'])
        self.assertEqual(evaluate(DummyNode(), '(1,"2") product || ("3",x)'), ['13', '1x', '23', '2x'])
        self.assertEqual(evaluate(DummyNode(), '(1,2) product || ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() product || (1.2)'), [])


if __name__ == '__main__':
    unittest.main()
