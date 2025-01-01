import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_equal_single_vs_matcher(self):
        self.assertEqual(evaluate(DummyPath(), '"5"=s"5"'), True)
        self.assertEqual(evaluate(DummyPath(), '"5"=~4:6'), True)
        self.assertEqual(evaluate(DummyPath(), '"5"=~5'), True)
        self.assertEqual(evaluate(DummyPath(), '"5"=~5@0.001'), True)

        self.assertEqual(evaluate(DummyPath(), '5=s"5"'), False)
        self.assertEqual(evaluate(DummyPath(), '5=~4:6'), True)
        self.assertEqual(evaluate(DummyPath(), '5=~5'), True)
        self.assertEqual(evaluate(DummyPath(), '5=~5@0.001'), True)
        self.assertEqual(evaluate(DummyPath(), '5=r"4|5|6"'), True)
        self.assertEqual(evaluate(DummyPath(), '5=g"[456]"'), True)

        self.assertEqual(evaluate(DummyPath(), '5.0=s"5"'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0=~4:6'), True)
        self.assertEqual(evaluate(DummyPath(), '5.0=~5'), True)
        self.assertEqual(evaluate(DummyPath(), '5.0=~5@0.001'), True)
        self.assertEqual(evaluate(DummyPath(), '5.0=r"4|5|6"'), True)
        self.assertEqual(evaluate(DummyPath(), '5.0=g"[456]"'), True)

    def test_must_equal_matcher_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), 's"5"="5"'), True)
        self.assertEqual(evaluate(DummyPath(), '~4:6="5"'), True)
        self.assertEqual(evaluate(DummyPath(), '~5="5"'), True)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001="5"'), True)

        self.assertEqual(evaluate(DummyPath(), 's"5"=5'), False)
        self.assertEqual(evaluate(DummyPath(), '~4:6=5'), True)
        self.assertEqual(evaluate(DummyPath(), '~5=5'), True)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001=5'), True)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"=5'), True)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"=5'), True)

        self.assertEqual(evaluate(DummyPath(), 's"5"=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~4:6=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~5=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"=5.0'), True)

    def test_must_equal_list_vs_matcher(self):
        self.assertEqual(evaluate(DummyPath(), '{"5","9"} zip sequence = s"5"'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{"5","9"} zip sequence = ~4:6'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{"5","9"} zip sequence = ~5'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{"5","9"} zip sequence = ~5@0.001'), [True, False])

        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = s"5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = ~4:6'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = ~5'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = ~5@0.001'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = r"4|5|6"'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5,9} zip sequence = g"[456]"'), [True, False])

        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = s"5"'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = ~4:6'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = ~5'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = ~5@0.001'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = r"4|5|6"'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '{5.0,9.0} zip sequence = g"[456]"'), [True, False])

    def test_must_equal_matcher_vs_list(self):
        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence = {"5","9"}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence = {"5","9"}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence = {"5","9"}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence = {"5","9"}'), [True, False])

        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence = {5,9}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence = {5,9}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence = {5,9}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence = {5,9}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6" zip sequence = {5,9}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), 'g"[456]" zip sequence = {5,9}'), [True, False])

        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence = {5.0,9.0}'), [False, False])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence = {5.0,9.0}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence = {5.0,9.0}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence = {5.0,9.0}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6" zip sequence = {5.0,9.0}'), [True, False])
        self.assertEqual(evaluate(DummyPath(), 'g"[456]" zip sequence = {5.0,9.0}'), [True, False])

        self.assertEqual(evaluate(DummyPath(), 's"5"=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~4:6=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~5=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"=5.0'), True)


if __name__ == '__main__':
    unittest.main()
