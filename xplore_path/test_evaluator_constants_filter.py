import unittest

from paths.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_extract_by_index_when_evaluates_to_single_number(self):
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][0]'), [5])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][1]'), [7])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][1+1]'), [9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][2]'), [9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][2.0]'), [9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][3]'), [])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][-1]'), [])

    def test_must_extract_when_evaluates_to_true(self):
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][. = 7]'), [7])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][. >= 7]'), [7, 9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][. = 100]'), [])

    def test_must_extract_when_evaluates_to_non_empty_node_set(self):
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][[100]]'), [5, 7, 9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][[100,200,300]]'), [5, 7, 9])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][[-555]]'), [5, 7, 9])

    def test_must_not_extract_when_evaluates_to_empty_node_set(self):
        self.assertEqual(evaluate(DummyPath(), '[5,7,9][[]]'), [])

    def test_must_extract_when_evaluates_to_string_and_that_coerced_string_matches_a_child(self):
        self.assertEqual(evaluate(DummyPath(), '[5,7,9]["8"]'), [])
        self.assertEqual(evaluate(DummyPath(), '[5,7,9]["7"]'), [7])


if __name__ == '__main__':
    unittest.main()
