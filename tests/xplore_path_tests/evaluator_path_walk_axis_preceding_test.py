import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/ptrs/preceding::*').unpack],
            [
                tuple(),
                ('a', ),
                ('a', 'b'),
                ('a', 'b', 'c'),
                ('a', 'b', 'd'),
                ('a', 'b', 'e'),
                ('a', 'b', 'f'),
                ('y', ),
                ('z', ),
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/ptrs/f_ptr/preceding::*').unpack],
            [
                tuple(),
                ('a', ),
                ('a', 'b'),
                ('a', 'b', 'c'),
                ('a', 'b', 'd'),
                ('a', 'b', 'e'),
                ('a', 'b', 'f'),
                ('y', ),
                ('z', ),
                ('ptrs', ),
                ('ptrs', 'd_ptr'),
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/ptrs/f_ptr/preceding::(label .)').unpack],
            [
                tuple(),
                ('a', ),
                ('a', 'b'),
                ('a', 'b', 'c'),
                ('a', 'b', 'd'),
                ('a', 'b', 'e'),
                ('a', 'b', 'f'),
                ('y', ),
                ('z', ),
                ('ptrs', ),
                ('ptrs', 'd_ptr'),
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/ptrs/f_ptr/preceding::e').unpack],
            [
                ('a', 'b', 'e')
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/preceding::*').unpack],
            []  # nothing is preceding the root node
        )


if __name__ == '__main__':
    unittest.main()
