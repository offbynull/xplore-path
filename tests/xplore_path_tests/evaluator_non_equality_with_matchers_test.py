import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_not_equal_single_vs_matcher(self):
        self.assertEqual(evaluate(DummyNode(), '"5"!=s"5"'), False)
        self.assertEqual(evaluate(DummyNode(), '"5"!=~4:6'), False)
        self.assertEqual(evaluate(DummyNode(), '"5"!=~5'), False)
        self.assertEqual(evaluate(DummyNode(), '"5"!=~5@0.001'), False)

        self.assertEqual(evaluate(DummyNode(), '5!=s"5"'), True)
        self.assertEqual(evaluate(DummyNode(), '5!=~4:6'), False)
        self.assertEqual(evaluate(DummyNode(), '5!=~5'), False)
        self.assertEqual(evaluate(DummyNode(), '5!=~5@0.001'), False)
        self.assertEqual(evaluate(DummyNode(), '5!=r"4|5|6"'), False)
        self.assertEqual(evaluate(DummyNode(), '5!=g"[456]"'), False)

        self.assertEqual(evaluate(DummyNode(), '5.0!=s"5"'), True)
        self.assertEqual(evaluate(DummyNode(), '5.0!=~4:6'), False)
        self.assertEqual(evaluate(DummyNode(), '5.0!=~5'), False)
        self.assertEqual(evaluate(DummyNode(), '5.0!=~5@0.001'), False)
        self.assertEqual(evaluate(DummyNode(), '5.0!=r"4|5|6"'), False)
        self.assertEqual(evaluate(DummyNode(), '5.0!=g"[456]"'), False)

    def test_must_not_equal_matcher_vs_single(self):
        self.assertEqual(evaluate(DummyNode(), 's"5"!="5"'), False)
        self.assertEqual(evaluate(DummyNode(), '~4:6!="5"'), False)
        self.assertEqual(evaluate(DummyNode(), '~5!="5"'), False)
        self.assertEqual(evaluate(DummyNode(), '~5@0.001!="5"'), False)

        self.assertEqual(evaluate(DummyNode(), 's"5"!=5'), True)
        self.assertEqual(evaluate(DummyNode(), '~4:6!=5'), False)
        self.assertEqual(evaluate(DummyNode(), '~5!=5'), False)
        self.assertEqual(evaluate(DummyNode(), '~5@0.001!=5'), False)
        self.assertEqual(evaluate(DummyNode(), 'r"4|5|6"!=5'), False)
        self.assertEqual(evaluate(DummyNode(), 'g"[456]"!=5'), False)

        self.assertEqual(evaluate(DummyNode(), 's"5"!=5.0'), True)
        self.assertEqual(evaluate(DummyNode(), '~4:6!=5.0'), False)
        self.assertEqual(evaluate(DummyNode(), '~5!=5.0'), False)
        self.assertEqual(evaluate(DummyNode(), '~5@0.001!=5.0'), False)
        self.assertEqual(evaluate(DummyNode(), 'r"4|5|6"!=5.0'), False)
        self.assertEqual(evaluate(DummyNode(), 'g"[456]"!=5.0'), False)

    def test_must_not_equal_list_vs_matcher(self):
        self.assertEqual(evaluate(DummyNode(), '("5","9") product sequence != s"5"'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '("5","9") product sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '("5","9") product sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '("5","9") product sequence != ~5@0.001'), [False, True])

        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != s"5"'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != ~5@0.001'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != r"4|5|6"'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5,9) product sequence != g"[456]"'), [False, True])

        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != s"5"'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != ~4:6'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != ~5'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != ~5@0.001'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != r"4|5|6"'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '(5.0,9.0) product sequence != g"[456]"'), [False, True])

    def test_must_not_equal_matcher_vs_list(self):
        self.assertEqual(evaluate(DummyNode(), 's"5" product sequence != ("5","9")'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~4:6 product sequence != ("5","9")'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5 product sequence != ("5","9")'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5@0.001 product sequence != ("5","9")'), [False, True])

        self.assertEqual(evaluate(DummyNode(), 's"5" product sequence != (5,9)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '~4:6 product sequence != (5,9)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5 product sequence != (5,9)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5@0.001 product sequence != (5,9)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), 'r"4|5|6" product sequence != (5,9)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), 'g"[456]" product sequence != (5,9)'), [False, True])

        self.assertEqual(evaluate(DummyNode(), 's"5" product sequence != (5.0,9.0)'), [True, True])
        self.assertEqual(evaluate(DummyNode(), '~4:6 product sequence != (5.0,9.0)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5 product sequence != (5.0,9.0)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), '~5@0.001 product sequence != (5.0,9.0)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), 'r"4|5|6" product sequence != (5.0,9.0)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), 'g"[456]" product sequence != (5.0,9.0)'), [False, True])


if __name__ == '__main__':
    unittest.main()
