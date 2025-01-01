import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_be_less_than_single_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), '5<5'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0<5'), False)
        self.assertEqual(evaluate(DummyPath(), '5<5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0<5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0<"5"'), False)
        self.assertEqual(evaluate(DummyPath(), '"5"<5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '"5"<"5"'), False)
        self.assertEqual(evaluate(DummyPath(), '5<4'), False)
        self.assertEqual(evaluate(DummyPath(), '5<"4"'), False)
        self.assertEqual(evaluate(DummyPath(), '5<6'), True)
        self.assertEqual(evaluate(DummyPath(), '5<"6"'), True)
        self.assertEqual(evaluate(DummyPath(), '5<x'), False)  # if it can't be coerced to be comparable, False
        self.assertEqual(evaluate(DummyPath(), 'x<5'), False)  # if it can't be coerced to be comparable, False

    def test_must_be_less_than_single_vs_seq_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyPath(), '5 zip sequence < {5,5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 zip sequence < {5,5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 zip sequence < {5.0,5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 zip sequence < {5.0,5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 zip sequence < {"5","5"}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '"5" zip sequence < {5.0, 5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '"5" zip sequence < {"5", "5"}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 zip sequence < {x, 5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 zip sequence < {x, 1}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 zip sequence < {}'), [])

    def test_must_be_less_than_single_vs_seq_using_zip_any(self):
        self.assertEqual(evaluate(DummyPath(), '5 zip any < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip any < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip any < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip any < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip any < {"5","5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" zip any < {5.0, 5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" zip any < {"5", "5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip any < {x, 5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip any < {x, 1}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip any < {}'), False)

    def test_must_be_less_than_single_vs_seq_using_zip_all(self):
        self.assertEqual(evaluate(DummyPath(), '5 zip all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip all < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip all < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 zip all < {"5","5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" zip all < {5.0, 5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" zip all < {"5", "5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip all < {x, 5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip all < {x, 1}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 zip all < {}'), True)

    def test_must_be_less_than_single_vs_seq_using_product_sequence(self):
        self.assertEqual(evaluate(DummyPath(), '5 product sequence < {5,5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 product sequence < {5,5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 product sequence < {5.0,5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 product sequence < {5.0,5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5.0 product sequence < {"5","5"}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '"5" product sequence < {5.0, 5.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '"5" product sequence < {"5", "5"}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 product sequence < {x, 5}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 product sequence < {x, 1}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '5 product sequence < {}'), [])

    def test_must_be_less_than_single_vs_seq_using_product_any(self):
        self.assertEqual(evaluate(DummyPath(), '5 product any < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product any < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product any < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product any < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product any < {"5","5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" product any < {5.0, 5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" product any < {"5", "5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product any < {x, 5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product any < {x, 1}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product any < {}'), False)

    def test_must_be_less_than_single_vs_seq_using_product_all(self):
        self.assertEqual(evaluate(DummyPath(), '5 product all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product all < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product all < {5.0,5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0 product all < {"5","5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" product all < {5.0, 5.0}'), False)
        self.assertEqual(evaluate(DummyPath(), '"5" product all < {"5", "5"}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product all < {x, 5}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product all < {x, 1}'), False)
        self.assertEqual(evaluate(DummyPath(), '5 product all < {}'), True)

    def test_must_be_less_than_seq_vs_single_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} zip sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} zip sequence < "5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} zip sequence < "5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{x, 5} zip sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{x, 1} zip sequence < 5'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '{} zip sequence < 5'), [])

    def test_must_be_less_than_seq_vs_single_using_zip_any(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} zip any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} zip any < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} zip any < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 5} zip any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 1} zip any < 5'), True)
        self.assertEqual(evaluate(DummyPath(), '{} zip any < 5'), False)

    def test_must_be_less_than_seq_vs_single_using_zip_all(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} zip all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} zip all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} zip all < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} zip all < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 5} zip all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 1} zip all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{} zip all < 5'), True)

    def test_must_be_less_than_seq_vs_single_using_product_sequence(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} product sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5,5} product sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} product sequence < 5.0'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} product sequence < "5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} product sequence < "5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{x, 5} product sequence < 5'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{x, 1} product sequence < 5'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '{} product sequence < 5'), [])

    def test_must_be_less_than_seq_vs_single_using_product_any(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} product any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} product any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} product any < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} product any < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} product any < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 5} product any < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 1} product any < 5'), True)
        self.assertEqual(evaluate(DummyPath(), '{} product any < 5'), False)

    def test_must_be_less_than_seq_vs_single_using_product_all(self):
        self.assertEqual(evaluate(DummyPath(), '{5,5} product all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} product all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,5.0} product all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5","5"} product all < 5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0, 5.0} product all < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{"5", "5"} product all < "5"'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 5} product all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{x, 1} product all < 5'), False)
        self.assertEqual(evaluate(DummyPath(), '{} product all < 5'), True)

    def test_must_be_less_than_seq_vs_seq_using_zip_sequence(self):
        self.assertEqual(evaluate(DummyPath(), '{5,4,3} zip sequence < {5,5}'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < {5,4,3}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,"4",3} zip sequence < {5,5}'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < {5.0,"4",3}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < {x,4}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{x,4} zip sequence < {5,5}'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip sequence < {}'), [])
        self.assertEqual(evaluate(DummyPath(), '{} zip sequence < {5,5}'), [])

    def test_must_be_less_than_seq_vs_seq_using_zip_any(self):
        self.assertEqual(evaluate(DummyPath(), '{5,4,3} zip any < {5,5}'), True)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < {5,4,3}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,"4",3} zip any < {5,5}'), True)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < {5.0,"4",3}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < {x,4}'), False)
        self.assertEqual(evaluate(DummyPath(), '{x,4} zip any < {5,5}'), True)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip any < {}'), False)
        self.assertEqual(evaluate(DummyPath(), '{} zip any < {5,5}'), False)

    def test_must_be_less_than_seq_vs_seq_using_zip_all(self):
        self.assertEqual(evaluate(DummyPath(), '{5,4,3} zip all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < {5,4,3}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5.0,"4",3} zip all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < {5.0,"4",3}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < {x,4}'), False)
        self.assertEqual(evaluate(DummyPath(), '{x,4} zip all < {5,5}'), False)
        self.assertEqual(evaluate(DummyPath(), '{5,5} zip all < {}'), True)
        self.assertEqual(evaluate(DummyPath(), '{} zip all < {5,5}'), True)


if __name__ == '__main__':
    unittest.main()
