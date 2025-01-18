import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(
            [e.label() for e in evaluate(root, '/a/descendant-or-self::f').unpack],
            ['f']
        )
        self.assertEqual(
            sorted([e.full_label() for e in evaluate(root, '/a/descendant-or-self::(label .)').unpack]),
            sorted([e.full_label() for e in evaluate(root, '/a').unpack] + [e.full_label() for e in evaluate(root, '/a//*').unpack])
        )
        self.assertEqual(
            sorted([e.full_label() for e in evaluate(root, '/descendant-or-self::*').unpack]),
            sorted([e.full_label() for e in evaluate(root, '.').unpack] + [e.full_label() for e in evaluate(root, '//*').unpack])
        )


if __name__ == '__main__':
    unittest.main()
