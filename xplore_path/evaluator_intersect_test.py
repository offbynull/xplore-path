import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_intersect_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), 'true intersect true'), [True])
        self.assertEqual(evaluate(DummyPath(), 'false intersect true'), [])
        self.assertEqual(evaluate(DummyPath(), '5 intersect 4'), [])
        self.assertEqual(evaluate(DummyPath(), '5 intersect 5'), [5])
        self.assertEqual(evaluate(DummyPath(), '5 intersect 5.0'), [5])
        self.assertEqual(evaluate(DummyPath(), '5 intersect "5"'), [])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type

    def test_must_intersect_single_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '5 intersect {5,1,9}'), [5])
        self.assertEqual(evaluate(DummyPath(), '5 intersect {5,1,"9"}'), [5])
        self.assertEqual(evaluate(DummyPath(), '5 intersect {}'), [])

    def test_must_intersect_seq_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '{5,1,9} intersect 5'), [5])
        self.assertEqual(evaluate(DummyPath(), '{5,1,"9"} intersect 5'), [5])
        self.assertEqual(evaluate(DummyPath(), '{} intersect 5'), [])

    def test_must_intersect_seq_vs_seq(self):
        self.assertEqual(sorted(evaluate(DummyPath(), '{5,7,9} intersect {5,1,9}')), [5, 9])
        self.assertEqual(sorted(evaluate(DummyPath(), '{5,7,9} intersect {5,1,"9"}')), [5])  # THIS IS WHAT XPATH DOES - no coercing before matching - intersects with just data and type
        self.assertEqual(sorted(evaluate(DummyPath(), '{5,7,9} intersect {}')), [])
        self.assertEqual(sorted(evaluate(DummyPath(), '{} intersect {5,7,9}')), [])


if __name__ == '__main__':
    unittest.main()
