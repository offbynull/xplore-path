import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_evaluate_to_self(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(evaluate(root, '.'), [root])
        self.assertEqual(evaluate(root, '/'), [root])
        self.assertEqual(evaluate(root, '/.'), [root])
        self.assertEqual(evaluate(root, '.'), [root])

    def test_must_walk_to_self_using_dot(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/.')], [[None, 'a']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/.')], [[None, 'a', 'b']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/c/.')], [[None, 'a', 'b', 'c']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/d/.')], [[None, 'a', 'b', 'd']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/xxx/.')], [])


if __name__ == '__main__':
    unittest.main()
