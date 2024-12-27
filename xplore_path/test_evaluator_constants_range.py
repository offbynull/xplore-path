import unittest

from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_produce_range(self):
        root = {}
        self.assertEqual(evaluate(root, '0 to 5'), [0, 1, 2, 3, 4, 5])
        self.assertEqual(evaluate(root, '5 to 5'), [5])
        self.assertEqual(evaluate(root, '6 to 5'), [])
        self.assertEqual(evaluate(root, '-1 to 5'), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(evaluate(root, '-1 to "5"'), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(evaluate(root, '"-1" to 5'), [-1, 0, 1, 2, 3, 4, 5])
        self.assertEqual(evaluate(root, '-1 to x'), [])
        self.assertEqual(evaluate(root, 'x to 5'), [])



if __name__ == '__main__':
    unittest.main()
