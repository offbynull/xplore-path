import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_multiply_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '5*5'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '5.0*5'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '5*5.0'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '5.0*5.0'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '5.0*"5"'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '"5"*5.0'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '"5"*"5"'), 25.0)
        self.assertEqual(evaluate(DummyPath(), '5*x'), [])

    def test_must_multiply_single_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '5*{5,6}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '5.0*{5,6}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '5*{5.0,6.0}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '5.0*{5.0,6.0}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '5.0*{"5","6"}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '"5"*{5.0, 6.0}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '"5"*{"5", "6"}'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '5*{x, 6}'), [30.0])
        self.assertEqual(evaluate(DummyPath(), '5*{}'), [])

    def test_must_multiply_seq_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '{5,6}*5'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{5,6}*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{5.0,6.0}*5'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{5.0,6.0}*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{"5","6"}*5.0'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{5.0, 6.0}*"5"'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{"5", "6"}*"5"'), [25.0, 30.0])
        self.assertEqual(evaluate(DummyPath(), '{x, 6}*5'), [30.0])
        self.assertEqual(evaluate(DummyPath(), '{}*5'), [])

    def test_must_multiply_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '{1,2}*{3,4}'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"}*{"3",4.0}'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"}*{"3",x}'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '{1,2}*{}'), [])
        self.assertEqual(evaluate(DummyPath(), '{}*{1.2}'), [])

    def test_must_multiply_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyPath(), '{1,2} zip * {3,4}'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"} zip * {"3",4.0}'), [3.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"} zip * {"3",x}'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '{1,2} zip * {}'), [])
        self.assertEqual(evaluate(DummyPath(), '{} zip * {1.2}'), [])

    def test_must_multiply_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyPath(), '{1,2} product * {3,4}'), [3.0, 4.0, 6.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"} product * {"3",4.0}'), [3.0, 4.0, 6.0, 8.0])
        self.assertEqual(evaluate(DummyPath(), '{1,"2"} product * {"3",x}'), [3.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '{1,2} product * {}'), [])
        self.assertEqual(evaluate(DummyPath(), '{} product * {1.2}'), [])


if __name__ == '__main__':
    unittest.main()
