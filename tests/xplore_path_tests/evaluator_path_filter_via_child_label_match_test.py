import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_label(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[d]').unpack],
            [
                ['a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[f]').unpack],
            [
                ['a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[FAKE]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[a]').unpack],
            [
                []
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[y]').unpack],
            [
                []
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[z]').unpack],
            [
                []
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[ptrs]').unpack],
            [
                []
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[MISSING]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[99]').unpack],  # first tries to grab value at index 99
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/["99"]').unpack],  # doesn't try to do index, goes to '99' directly
            [
                []
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[b]/b[c]/e').unpack],
            [
                ['a', 'b', 'e']
            ]
        )

    def test_must_filter_based_on_label_using_matchers(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[s"d"]').unpack],
            [
                ['a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[g"[fz]"]').unpack],
            [
                ['a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[r"[fz]"]').unpack],
            [
                ['a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[r"[z]"]').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/*[~1:2]').unpack],  # PULLS OUT INDEX 1:2
            [
                ['y'],
                ['z']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[~98:100]').unpack],  # BECAUSE INDEX IS OUT OF RANGE
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[g"b"]/b[r"c"]/e').unpack],
            [
                ['a', 'b', 'e']
            ]
        )


if __name__ == '__main__':
    unittest.main()
