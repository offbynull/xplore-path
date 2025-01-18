import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_be_greater_than_or_equal_single_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), '5>=5'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0>=5'), True)
        self.assertEqual(evaluate(DummyNode(), '5>=5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0>=5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0>="5"'), True)
        self.assertEqual(evaluate(DummyNode(), '"5">=5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '"5">="5"'), True)
        self.assertEqual(evaluate(DummyNode(), '5>=4'), True)
        self.assertEqual(evaluate(DummyNode(), '5>="4"'), True)
        self.assertEqual(evaluate(DummyNode(), '5>=6'), False)
        self.assertEqual(evaluate(DummyNode(), '5>="6"'), False)
        self.assertEqual(evaluate(DummyNode(), '5>=x'), False)  # if it can't be coerced to be comparable, False
        self.assertEqual(evaluate(DummyNode(), 'x>=5'), False)  # if it can't be coerced to be comparable, False

    def test_must_be_greater_than_or_equal_single_vs_seq_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyNode(), '5 zip sequence >= (5,5)'), [True])
        self.assertEqual(evaluate(DummyNode(), '5.0 zip sequence >= (5,5)'), [True])
        self.assertEqual(evaluate(DummyNode(), '5 zip sequence >= (5.0,5.0)'), [True])
        self.assertEqual(evaluate(DummyNode(), '5.0 zip sequence >= (5.0,5.0)'), [True])
        self.assertEqual(evaluate(DummyNode(), '5.0 zip sequence >= ("5","5")'), [True])
        self.assertEqual(evaluate(DummyNode(), '"5" zip sequence >= (5.0, 5.0)'), [True])
        self.assertEqual(evaluate(DummyNode(), '"5" zip sequence >= ("5", "5")'), [True])
        self.assertEqual(evaluate(DummyNode(), '5 zip sequence >= (x, 5)'), [False])
        self.assertEqual(evaluate(DummyNode(), '5 zip sequence >= (x, 1)'), [False])
        self.assertEqual(evaluate(DummyNode(), '5 zip sequence >= ()'), [])

    def test_must_be_greater_than_or_equal_single_vs_seq_using_zip_any(self):
        self.assertEqual(evaluate(DummyNode(), '5 zip any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 zip any >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip any >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip any >= ("5","5")'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" zip any >= (5.0, 5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" zip any >= ("5", "5")'), True)
        self.assertEqual(evaluate(DummyNode(), '5 zip any >= (x, 5)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 zip any >= (x, 1)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 zip any >= ()'), False)

    def test_must_be_greater_than_or_equal_single_vs_seq_using_zip_all(self):
        self.assertEqual(evaluate(DummyNode(), '5 zip all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 zip all >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip all >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 zip all >= ("5","5")'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" zip all >= (5.0, 5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" zip all >= ("5", "5")'), True)
        self.assertEqual(evaluate(DummyNode(), '5 zip all >= (x, 5)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 zip all >= (x, 1)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 zip all >= ()'), True)

    def test_must_be_greater_than_or_equal_single_vs_seq_using_product_sequence(self):
        self.assertEqual(evaluate(DummyNode(), '5 product sequence >= (5,5)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '5.0 product sequence >= (5,5)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '5 product sequence >= (5.0,5.0)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '5.0 product sequence >= (5.0,5.0)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '5.0 product sequence >= ("5","5")'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '"5" product sequence >= (5.0, 5.0)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '"5" product sequence >= ("5", "5")'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '5 product sequence >= (x, 5)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '5 product sequence >= (x, 1)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '5 product sequence >= ()'), [])

    def test_must_be_greater_than_or_equal_single_vs_seq_using_product_any(self):
        self.assertEqual(evaluate(DummyNode(), '5 product any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product any >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product any >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product any >= ("5","5")'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" product any >= (5.0, 5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" product any >= ("5", "5")'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product any >= (x, 5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product any >= (x, 1)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product any >= ()'), False)

    def test_must_be_greater_than_or_equal_single_vs_seq_using_product_all(self):
        self.assertEqual(evaluate(DummyNode(), '5 product all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product all >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product all >= (5.0,5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0 product all >= ("5","5")'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" product all >= (5.0, 5.0)'), True)
        self.assertEqual(evaluate(DummyNode(), '"5" product all >= ("5", "5")'), True)
        self.assertEqual(evaluate(DummyNode(), '5 product all >= (x, 5)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 product all >= (x, 1)'), False)
        self.assertEqual(evaluate(DummyNode(), '5 product all >= ()'), True)

    def test_must_be_greater_than_or_equal_seq_vs_single_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= 5'), [True])
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= 5.0'), [True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip sequence >= 5'), [True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip sequence >= 5.0'), [True])
        self.assertEqual(evaluate(DummyNode(), '("5","5") zip sequence >= 5.0'), [True])
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) zip sequence >= "5"'), [True])
        self.assertEqual(evaluate(DummyNode(), '("5", "5") zip sequence >= "5"'), [True])
        self.assertEqual(evaluate(DummyNode(), '(x, 5) zip sequence >= 5'), [False])
        self.assertEqual(evaluate(DummyNode(), '(x, 1) zip sequence >= 5'), [False])
        self.assertEqual(evaluate(DummyNode(), '() zip sequence >= 5'), [])

    def test_must_be_greater_than_or_equal_seq_vs_single_using_zip_any(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip any >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '("5","5") zip any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) zip any >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '("5", "5") zip any >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '(x, 5) zip any >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '(x, 1) zip any >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '() zip any >= 5'), False)

    def test_must_be_greater_than_or_equal_seq_vs_single_using_zip_all(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip all >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) zip all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '("5","5") zip all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) zip all >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '("5", "5") zip all >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '(x, 5) zip all >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '(x, 1) zip all >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '() zip all >= 5'), True)

    def test_must_be_greater_than_or_equal_seq_vs_single_using_product_sequence(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) product sequence >= 5'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5,5) product sequence >= 5.0'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product sequence >= 5'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product sequence >= 5.0'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '("5","5") product sequence >= 5.0'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) product sequence >= "5"'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '("5", "5") product sequence >= "5"'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(x, 5) product sequence >= 5'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(x, 1) product sequence >= 5'), [False, False])
        self.assertEqual(evaluate(DummyNode(), '() product sequence >= 5'), [])

    def test_must_be_greater_than_or_equal_seq_vs_single_using_product_any(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) product any >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) product any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product any >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '("5","5") product any >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) product any >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '("5", "5") product any >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '(x, 5) product any >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(x, 1) product any >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '() product any >= 5'), False)

    def test_must_be_greater_than_or_equal_seq_vs_single_using_product_all(self):
        self.assertEqual(evaluate(DummyNode(), '(5,5) product all >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) product all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product all >= 5'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,5.0) product all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '("5","5") product all >= 5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0, 5.0) product all >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '("5", "5") product all >= "5"'), True)
        self.assertEqual(evaluate(DummyNode(), '(x, 5) product all >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '(x, 1) product all >= 5'), False)
        self.assertEqual(evaluate(DummyNode(), '() product all >= 5'), True)

    def test_must_be_greater_than_or_equal_seq_vs_seq_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyNode(), '(5,6,7) zip sequence >= (5,5)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= (5,6,7)'), [True, False])
        self.assertEqual(evaluate(DummyNode(), '(5.0,"6",7) zip sequence >= (5,5)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= (5.0,"6",7)'), [True, False])
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= (x,6)'), [False, False])
        self.assertEqual(evaluate(DummyNode(), '(x,6) zip sequence >= (5,5)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip sequence >= ()'), [])
        self.assertEqual(evaluate(DummyNode(), '() zip sequence >= (5,5)'), [])

    def test_must_be_greater_than_or_equal_seq_vs_seq_using_zip_any(self):
        self.assertEqual(evaluate(DummyNode(), '(5,6,7) zip any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= (5,6,7)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5.0,"6",7) zip any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= (5.0,"6",7)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= (x,6)'), False)
        self.assertEqual(evaluate(DummyNode(), '(x,6) zip any >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip any >= ()'), False)
        self.assertEqual(evaluate(DummyNode(), '() zip any >= (5,5)'), False)

    def test_must_be_greater_than_or_equal_seq_vs_seq_using_zip_all(self):
        self.assertEqual(evaluate(DummyNode(), '(5,6,7) zip all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= (5,6,7)'), False)
        self.assertEqual(evaluate(DummyNode(), '(5.0,"6",7) zip all >= (5,5)'), True)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= (5.0,"6",7)'), False)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= (x,6)'), False)
        self.assertEqual(evaluate(DummyNode(), '(x,6) zip all >= (5,5)'), False)
        self.assertEqual(evaluate(DummyNode(), '(5,5) zip all >= ()'), True)
        self.assertEqual(evaluate(DummyNode(), '() zip all >= (5,5)'), True)


if __name__ == '__main__':
    unittest.main()
