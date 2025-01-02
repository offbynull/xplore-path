import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_divide_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '25 div 5'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '25.0 div 5'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '25 div 5.0'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '25.0 div 5.0'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '25.0 div "5"'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '"25" div 5.0'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '"25" div "5"'), 5.0)
        self.assertEqual(evaluate(DummyPath(), '25 div x'), [])

    def test_must_divide_single_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '30 div (5,6)'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 div (5,6)'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30 div (5.0,6.0)'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 div (5.0,6.0)'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30.0 div ("5","6")'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '"30" div (5.0, 6.0)'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '"30" div ("5", "6")'), [6.0, 5.0])
        self.assertEqual(evaluate(DummyPath(), '30 div (x, 6)'), [5.0])
        self.assertEqual(evaluate(DummyPath(), '30 div ()'), [])

    def test_must_divide_seq_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '(25,30) div 5'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '(25,30) div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '(25.0,30.0) div 5'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '(25.0,30.0) div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '("25","30") div 5.0'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '(25.0, 30.0) div "5"'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '("25", "30") div "5"'), [5.0, 6.0])
        self.assertEqual(evaluate(DummyPath(), '(x, 30) div 5'), [6.0])
        self.assertEqual(evaluate(DummyPath(), '() div 5'), [])

    def test_must_divide_seq_vs_seq(self):
        self.assertEqual(evaluate(DummyPath(), '(6,8) div (2,4)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") div ("2",4.0)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") div ("2",x)'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '(6,8) div ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() div (1.2)'), [])

    def test_must_divide_seq_vs_seq_using_zip(self):
        self.assertEqual(evaluate(DummyPath(), '(6,8) zip div (2,4)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") zip div ("2",4.0)'), [3.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") zip div ("2",x)'), [3.0])
        self.assertEqual(evaluate(DummyPath(), '(6,8) zip div ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() zip div (1.2)'), [])

    def test_must_divide_seq_vs_seq_using_product(self):
        self.assertEqual(evaluate(DummyPath(), '(6,8) product div (2,4)'), [3.0, 1.5, 4.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") product div ("2",4.0)'), [3.0, 1.5, 4.0, 2.0])
        self.assertEqual(evaluate(DummyPath(), '(6,"8") product div ("2",x)'), [3.0, 4.0])
        self.assertEqual(evaluate(DummyPath(), '(6,8) product div ()'), [])
        self.assertEqual(evaluate(DummyPath(), '() product div (1.2)'), [])


if __name__ == '__main__':
    unittest.main()
