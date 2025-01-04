import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_walk_to_descendant_directly(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.full_label() for e in evaluate(root, '//a')], [[None, 'a']])
        self.assertEqual([e.full_label() for e in evaluate(root, '//b')], [[None, 'a', 'b']])
        self.assertEqual([e.full_label() for e in evaluate(root, '//c')], [[None, 'a', 'b', 'c']])
        self.assertEqual([e.full_label() for e in evaluate(root, '//d')], [[None, 'a', 'b', 'd']])
        self.assertEqual([e.full_label() for e in evaluate(root, '//xxx')], [])

    def test_must_walk_to_descendant_from_sub_path(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.full_label() for e in evaluate(root, '/a//d')], [[None, 'a', 'b', 'd']])
        self.assertEqual([e.label() for e in evaluate(root, '/a//*')], ['b', 'c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b//*')], ['c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '/a//d')], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b//d')], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d//zzz')], [])

    def test_must_walk_to_descendant_using_wildcard(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '//*')], ['a', 'b', 'c', 'd', 'e', 'f', 'y', 'z', 'ptrs', 'd_ptr', 'f_ptr'])
        self.assertEqual([e.label() for e in evaluate(root, '/.//*')], ['a', 'b', 'c', 'd', 'e', 'f', 'y', 'z', 'ptrs', 'd_ptr', 'f_ptr'])
        self.assertEqual([e.label() for e in evaluate(root, '//a//*')], ['b', 'c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '//b//*')], ['c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '//c//*')], [])

    def test_must_walk_to_descendant_using_strict_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '//s"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '//s"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '//s"c"')], ["c"])

    def test_must_walk_to_descendant_using_regex_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '//"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '//r"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '//r"c|e|f"')], ['c', 'e', 'f', 'f_ptr'])

    def test_must_walk_to_descendant_using_glob_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '//g"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '//g"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '//g"[cef]"')], ['c', 'e', 'f'])

    def test_must_walk_to_descendant_using_fuzzy_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, 'hello': 3})
        self.assertEqual([e.label() for e in evaluate(root, '//f"fello"')], ['hello'])

    def test_must_walk_to_descendant_using_range_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {1: 'c', 2: 'd', -1: 'e', -2: 'f'}}})
        self.assertEqual([e.value() for e in evaluate(root, '//b/~-1:1')], ['c', 'e'])
        self.assertEqual([e.value() for e in evaluate(root, '//b/~(-1:1]')], ['c'])


if __name__ == '__main__':
    unittest.main()
