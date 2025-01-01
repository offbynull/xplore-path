import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_negate_single(self):
        self.assertEqual(evaluate(DummyPath(), '-5'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-5.0'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-"5"'), -5.0)
        self.assertEqual(evaluate(DummyPath(), '-"-5"'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '-x'), [])

    def test_must_negate_seq(self):
        self.assertEqual(evaluate(DummyPath(), '-{5, 6}'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-{5.0, 6}'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-{"5", 6}'), [-5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-{"-5", 6}'), [5.0, -6.0])
        self.assertEqual(evaluate(DummyPath(), '-{x, 6}'), [-6.0])
        self.assertEqual(evaluate(DummyPath(), '-{x}'), [])
        self.assertEqual(evaluate(DummyPath(), '-{}'), [])


if __name__ == '__main__':
    unittest.main()
