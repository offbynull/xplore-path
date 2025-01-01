import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_label(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, '99': 'bye'})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/c <= 0]')],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/c <= 1]')],
            [
                [None, 'a']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/d = ~1:2]')],
            [
                [None, 'a']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a[./b/d = ~[1:2)]')],
            []
        )


if __name__ == '__main__':
    unittest.main()
