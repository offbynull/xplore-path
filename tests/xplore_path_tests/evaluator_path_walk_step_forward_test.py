import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_walk_to_child_directly(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/a').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c').unpack], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d').unpack], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx').unpack], [])

    def test_must_walk_to_child_using_wildcard(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/*').unpack], ['a', 'y', 'z', 'ptrs'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/*').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*').unpack], ['c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/*').unpack], [])

    def test_must_walk_to_child_using_strict_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/s"a"').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/s"b"').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/s"c"').unpack], ["c"])

    def test_must_walk_to_child_using_regex_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/r"a"').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/r"b"').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/r"c|e|f"').unpack], ['c', 'e', 'f'])

    def test_must_walk_to_child_using_glob_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/g"a"').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/g"b"').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/g"[cef]"').unpack], ['c', 'e', 'f'])

    def test_must_walk_to_child_using_fuzzy_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, 'hello': 3})
        self.assertEqual([e.label() for e in evaluate(root, '/f"fello"').unpack], ['hello'])

    def test_must_walk_to_child_using_range_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {1: 'c', 2: 'd', -1: 'e', -2: 'f'}}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/~-1:1').unpack], ['c', 'e'])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/~(-1:1]').unpack], ['c'])


if __name__ == '__main__':
    unittest.main()
