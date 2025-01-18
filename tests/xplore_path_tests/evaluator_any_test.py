import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_evaluate_single_as_if_its_list_of_1(self):
        self.assertEqual(evaluate(DummyNode(), 'any a'), True)  # non-empty string coerces to true
        self.assertEqual(evaluate(DummyNode(), 'any ""'), False)  # empty string coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any 0'), False)  # 0 coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any nan'), False)  # nan coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any 1'), True)  # non-0 coerces to true
        self.assertEqual(evaluate(DummyNode(), 'any -1'), True)  # non-0 coerces to true (even if its negative)
        self.assertEqual(evaluate(DummyNode(), 'any true'), True)
        self.assertEqual(evaluate(DummyNode(), 'any false'), False)

    def test_must_evaluate_list_of_1(self):
        self.assertEqual(evaluate(DummyNode(), 'any (a)'), True)  # non-empty string coerces to true
        self.assertEqual(evaluate(DummyNode(), 'any ("")'), False)  # empty string coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any (0)'), False)  # 0 coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any (nan)'), False)  # nan coerces to false
        self.assertEqual(evaluate(DummyNode(), 'any (1)'), True)  # non-0 coerces to true
        self.assertEqual(evaluate(DummyNode(), 'any (-1)'), True)  # non-0 coerces to true (even if its negative)
        self.assertEqual(evaluate(DummyNode(), 'any (true)'), True)
        self.assertEqual(evaluate(DummyNode(), 'any (false)'), False)

    def test_must_evaluate_empty_list(self):
        self.assertEqual(evaluate(DummyNode(), 'any ()'), False)

    def test_must_evaluate_list_of_many(self):
        self.assertEqual(evaluate(DummyNode(), 'any ("", 0, nan, false)'), False)  # all coerce to false
        self.assertEqual(evaluate(DummyNode(), 'any ("", 0, nan, false, true)'), True)  # one coerces to true
        self.assertEqual(evaluate(DummyNode(), 'any ("a", 1, true)'), True)  # all coerce to true


if __name__ == '__main__':
    unittest.main()
