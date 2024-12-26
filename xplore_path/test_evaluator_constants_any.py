import unittest

from evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_evaluate_single_as_if_its_list_of_1(self):
        root = {}
        self.assertEqual(evaluate(root, 'any a'), True)  # non-empty string coerces to true
        self.assertEqual(evaluate(root, 'any ""'), False)  # empty string coerces to false
        self.assertEqual(evaluate(root, 'any 0'), False)  # 0 coerces to false
        self.assertEqual(evaluate(root, 'any nan'), False)  # nan coerces to false
        self.assertEqual(evaluate(root, 'any 1'), True)  # non-0 coerces to true
        self.assertEqual(evaluate(root, 'any -1'), True)  # non-0 coerces to true (even if its negative)
        self.assertEqual(evaluate(root, 'any true'), True)
        self.assertEqual(evaluate(root, 'any false'), False)

    def test_must_evaluate_list_of_1(self):
        root = {}
        self.assertEqual(evaluate(root, 'any [a]'), True)  # non-empty string coerces to true
        self.assertEqual(evaluate(root, 'any [""]'), False)  # empty string coerces to false
        self.assertEqual(evaluate(root, 'any [0]'), False)  # 0 coerces to false
        self.assertEqual(evaluate(root, 'any [nan]'), False)  # nan coerces to false
        self.assertEqual(evaluate(root, 'any [1]'), True)  # non-0 coerces to true
        self.assertEqual(evaluate(root, 'any [-1]'), True)  # non-0 coerces to true (even if its negative)
        self.assertEqual(evaluate(root, 'any [true]'), True)
        self.assertEqual(evaluate(root, 'any [false]'), False)

    def test_must_evaluate_empty_list(self):
        root = {}
        self.assertEqual(evaluate(root, 'any []'), False)

    def test_must_evaluate_list_of_many(self):
        root = {}
        self.assertEqual(evaluate(root, 'any ["", 0, nan, false]'), False)  # all coerce to false
        self.assertEqual(evaluate(root, 'any ["", 0, nan, false, true]'), True)  # one coerces to true
        self.assertEqual(evaluate(root, 'any ["a", 1, true]'), True)  # all coerce to true


if __name__ == '__main__':
    unittest.main()
