import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/ptrs/preceding-sibling::*').unpack],
            [
                ['a'],
                ['y'],
                ['z']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/preceding-sibling::*').unpack],
            [
                ['a','b','c'],
                ['a','b','d']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/preceding-sibling::(label .)').unpack],
            [
                ['a','b','c'],
                ['a','b','d']
            ]
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/a/b/e/preceding-sibling::a').unpack],
            []
        )
        self.assertEqual(
            [e.full_label() for e in evaluate(root, '/preceding-sibling::*').unpack],
            []  # nothing is preceding the root node
        )


if __name__ == '__main__':
    unittest.main()
