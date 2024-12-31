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

    def test_must_walk_to_child_directly(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a')], [root.value()['a']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx')], [])

    def test_must_walk_to_self_using_dot(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/.')], [root.value()['a']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/.')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/.')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/.')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/.')], [])

    def test_must_walk_to_self_using_self_directive(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/self::a')], [root.value()['a']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/self::b')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/self::c')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/self::d')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/self::xxx')], [])

    def test_must_walk_to_self_using_self_directive_taking_the_label_of_the_current_node(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/self::(label .)')], [root.value()['a']])  # self:: takes the values inside of its inner expr and uses those values to find matches
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/self::(label .)')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/self::(label .)')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/self::(label .)')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/self::(label .)')], [])
    #
    # continue here
    # continue here
    # continue here
    # continue here

    def test_must_walk_to_parent(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/..')], [])
        self.assertEqual([e.value() for e in evaluate(root, '/a/..')], [root.value()])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/..')], [root.value()['a']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/..')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/..')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/.')], [])

    def test_must_walk_to_child_using_wildcard(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/*')], ['a', 'y', 'z', 'ptrs'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/*')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*')], ['c', 'd', 'e', 'f'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/*')], [])

    def test_must_walk_to_child_using_strict_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/s"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/s"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/s"c"')], ["c"])

    def test_must_walk_to_child_using_regex_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/r"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/r"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/r"c|e|f"')], ['c', 'e', 'f'])

    def test_must_walk_to_child_using_glob_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/g"a"')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/g"b"')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/g"[cef]"')], ['c', 'e', 'f'])

    def test_must_walk_to_child_using_fuzzy_matcher(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}, 'hello': 3})
        self.assertEqual([e.label() for e in evaluate(root, '/f"fello"')], ['hello'])


if __name__ == '__main__':
    unittest.main()
