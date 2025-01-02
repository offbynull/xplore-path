import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_integer_divide_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '30 idiv 4'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv 4'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '30 idiv 4.0'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv 4.0'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv "4"'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '"30" idiv 4.0'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '"30" idiv "4"'), 7.0)
        self.assertEqual(evaluate(DummyPath(), '30 idiv x'), [])

    def test_must_integer_divide_single_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '30 idiv (4,6)'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv (4,6)'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30 idiv (4.0,6.0)'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv (4.0,6.0)'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 idiv ("4","6")'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '"30" idiv (4.0, 6.0)'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '"30" idiv ("4", "6")'), [7.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30 idiv (x, 6)'), [5.0])
        self.assertEqual(evaluate(DummyPath(), '30 idiv ()'), [])

    def test_must_integer_divide_seq_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '(30,25) idiv 6'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(30,25) idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(30.0,25.0) idiv 6'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(30.0,25.0) idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '("30","25") idiv 6.0'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(30.0, 25.0) idiv "6"'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '("30", "25") idiv "6"'), [5.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(x, 25) idiv 6'), [4.0])
        self.assertEqual(evaluate(DummyPath(), '() idiv 6'), [])

    def test_must_integer_divide_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '(7,8) idiv (2,3)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") idiv ("2",3.0)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") idiv ("2",x)'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '(7,8) idiv ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() idiv (1.2)'), [])

    def test_must_integer_divide_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyPath(), '(7,8) zip idiv (2,3)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") zip idiv ("2",3.0)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") zip idiv ("2",x)'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '(7,8) zip idiv ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() zip idiv (1.2)'), [])

    def test_must_integer_divide_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyPath(), '(7,8) product idiv (2,3)'), [3.0, 2.0, 4.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") product idiv ("2",3.0)'), [3.0, 2.0, 4.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(7,"8") product idiv ("2",x)'), [3.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(7,8) product idiv ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() product idiv (1.2)'), [])


if __name__ == '__main__':
    unittest.main()
