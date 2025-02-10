import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_apply_not_single(self):
        self.assertEqual(evaluate(DummyNode(), 'not true'), False)
        self.assertEqual(evaluate(DummyNode(), 'not false'), True)

        self.assertEqual(evaluate(DummyNode(), 'not a'), False)  # non-empty string coerces to true
        self.assertEqual(evaluate(DummyNode(), 'not ""'), True)  # empty string coerces to false

        self.assertEqual(evaluate(DummyNode(), 'not 0'), True)  # 0 coerces to false
        self.assertEqual(evaluate(DummyNode(), 'not 1'), False)  # 1 coerces to true
        self.assertEqual(evaluate(DummyNode(), 'not nan'), True)  # nan coerces to false

    def test_must_apply_not_seq(self):
        self.assertEqual(evaluate(DummyNode(), 'not (true, true)'), [False, False])
        self.assertEqual(evaluate(DummyNode(), 'not (true, false)'), [False, True])
        self.assertEqual(evaluate(DummyNode(), 'not (1, nan, "s", "")'), [False, True, False, True])
        self.assertEqual(evaluate(DummyNode(), 'not (1, "s", true)'), [False, False, False])
        self.assertEqual(evaluate(DummyNode(), 'not (0, nan, "")'), [True, True, True])
        self.assertEqual(evaluate(DummyNode(), 'not ()'), [])


if __name__ == '__main__':
    unittest.main()
