import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/following::*').unpack],
            [
                [None, 'y'],
                [None, 'z'],
                [None, 'ptrs'],
                [None, 'ptrs', 'd_ptr'],
                [None, 'ptrs', 'f_ptr'],
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/following::*').unpack],
            [
                [None, 'a','b','f'],
                [None, 'y'],
                [None, 'z'],
                [None, 'ptrs'],
                [None, 'ptrs', 'd_ptr'],
                [None, 'ptrs', 'f_ptr'],
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/following::(label .)').unpack],
            [
                [None, 'a','b','f'],
                [None, 'y'],
                [None, 'z'],
                [None, 'ptrs'],
                [None, 'ptrs', 'd_ptr'],
                [None, 'ptrs', 'f_ptr'],
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/following::ptrs').unpack],
            [
                [None, 'ptrs']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/following::*').unpack],
            []  # nothing is following the root node
        )


if __name__ == '__main__':
    unittest.main()
