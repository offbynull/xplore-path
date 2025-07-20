import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_label(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/c <= 0]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/c <= 1]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/d = ~1:2]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/d = ~[1:2)]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/d = ~1:2]/b[./d = 2]/e').unpack],
            [
                ('a', 'b', 'e')
            ]
        )


if __name__ == '__main__':
    unittest.main()
