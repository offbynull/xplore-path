import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_label(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/c]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/FAKE]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[/a]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[.//*]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[//*]').unpack],
            [
                ('a', )
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b]/b[./e]/d').unpack],
            [
                ('a', 'b', 'd', )
            ]
        )


if __name__ == '__main__':
    unittest.main()
