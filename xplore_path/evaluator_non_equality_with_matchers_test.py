import unittest

from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.evaluator import evaluate


class EvaluatorTest(unittest.TestCase):
    def test_must_not_equal_single_vs_matcher(self):
        self.assertEqual(evaluate(DummyPath(), '"5"!=s"5"'), False)
        self.assertEqual(evaluate(DummyPath(), '"5"!=~4:6'), False)
        self.assertEqual(evaluate(DummyPath(), '"5"!=~5'), False)
        self.assertEqual(evaluate(DummyPath(), '"5"!=~5@0.001'), False)

        self.assertEqual(evaluate(DummyPath(), '5!=s"5"'), True)
        self.assertEqual(evaluate(DummyPath(), '5!=~4:6'), False)
        self.assertEqual(evaluate(DummyPath(), '5!=~5'), False)
        self.assertEqual(evaluate(DummyPath(), '5!=~5@0.001'), False)
        self.assertEqual(evaluate(DummyPath(), '5!=r"4|5|6"'), False)
        self.assertEqual(evaluate(DummyPath(), '5!=g"[456]"'), False)

        self.assertEqual(evaluate(DummyPath(), '5.0!=s"5"'), True)
        self.assertEqual(evaluate(DummyPath(), '5.0!=~4:6'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0!=~5'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0!=~5@0.001'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0!=r"4|5|6"'), False)
        self.assertEqual(evaluate(DummyPath(), '5.0!=g"[456]"'), False)

    def test_must_not_equal_matcher_vs_single(self):
        self.assertEqual(evaluate(DummyPath(), 's"5"!="5"'), False)
        self.assertEqual(evaluate(DummyPath(), '~4:6!="5"'), False)
        self.assertEqual(evaluate(DummyPath(), '~5!="5"'), False)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001!="5"'), False)

        self.assertEqual(evaluate(DummyPath(), 's"5"!=5'), True)
        self.assertEqual(evaluate(DummyPath(), '~4:6!=5'), False)
        self.assertEqual(evaluate(DummyPath(), '~5!=5'), False)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001!=5'), False)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"!=5'), False)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"!=5'), False)

        self.assertEqual(evaluate(DummyPath(), 's"5"!=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~4:6!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~5!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"!=5.0'), False)

    def test_must_not_equal_list_vs_matcher(self):
        self.assertEqual(evaluate(DummyPath(), '["5","9"] zip sequence != s"5"'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '["5","9"] zip sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '["5","9"] zip sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '["5","9"] zip sequence != ~5@0.001'), [False, True])

        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != s"5"'), [True, True])
        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != ~5@0.001'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != r"4|5|6"'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5,9] zip sequence != g"[456]"'), [False, True])

        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != s"5"'), [True, True])
        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != ~5@0.001'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != r"4|5|6"'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '[5.0,9.0] zip sequence != g"[456]"'), [False, True])

    def test_must_not_equal_matcher_vs_list(self):
        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence != ["5","9"]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence != ["5","9"]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence != ["5","9"]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence != ["5","9"]'), [False, True])

        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence != [5,9]'), [True, True])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence != [5,9]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence != [5,9]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence != [5,9]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6" zip sequence != [5,9]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), 'g"[456]" zip sequence != [5,9]'), [False, True])

        self.assertEqual(evaluate(DummyPath(), 's"5" zip sequence != [5.0,9.0]'), [True, True])
        self.assertEqual(evaluate(DummyPath(), '~4:6 zip sequence != [5.0,9.0]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5 zip sequence != [5.0,9.0]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), '~5@0.001 zip sequence != [5.0,9.0]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6" zip sequence != [5.0,9.0]'), [False, True])
        self.assertEqual(evaluate(DummyPath(), 'g"[456]" zip sequence != [5.0,9.0]'), [False, True])

        self.assertEqual(evaluate(DummyPath(), 's"5"!=5.0'), True)
        self.assertEqual(evaluate(DummyPath(), '~4:6!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~5!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), '~5@0.001!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), 'r"4|5|6"!=5.0'), False)
        self.assertEqual(evaluate(DummyPath(), 'g"[456]"!=5.0'), False)


if __name__ == '__main__':
    unittest.main()
