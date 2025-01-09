import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_evaluate_to_empty_when_getting_parent_of_root(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(evaluate(root, '..'), [])

    def test_must_walk_to_parent(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/..')], [])
        self.assertEqual([e.label() for e in evaluate(root, '/a/..')], [None])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/..')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/..')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d/..')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/.')], [])


if __name__ == '__main__':
    unittest.main()
