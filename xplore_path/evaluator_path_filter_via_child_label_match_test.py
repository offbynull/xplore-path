import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_label(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[d]')],
            [
                [None, 'a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[f]')],
            [
                [None, 'a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[FAKE]')],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[a]')],
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[y]')],
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[z]')],
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[ptrs]')],
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[MISSING]')],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[99]')],  # first tries to grab value at index 99, if not exists it'll try to grab key 99 - the latter exists as a string
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/["99"]')],  # doesn't try to do index, goes to '99' directly
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[b]/b[c]/e')],
            [
                [None, 'a', 'b', 'e']
            ]
        )

    def test_must_filter_based_on_label_using_matchers(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[s"d"]')],
            [
                [None, 'a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[g"[fz]"]')],
            [
                [None, 'a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[r"[fz]"]')],
            [
                [None, 'a', 'b']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/*[r"[z]"]')],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/*[~1:2]')],  # PULLS OUT INDEX 1:2
            [
                [None, 'y'],
                [None, 'z']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/[~98:100]')],  # BECAUSE INDEX IS OUT OF RANGE, RETURNS IF CHILD WITH LABEL EXISTS
            [
                [None]
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[g"b"]/b[r"c"]/e')],
            [
                [None, 'a', 'b', 'e']
            ]
        )

if __name__ == '__main__':
    unittest.main()
