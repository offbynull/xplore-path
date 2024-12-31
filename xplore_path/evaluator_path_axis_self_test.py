import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_walk_to_self_using_self_directive(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/self::a')], [root.value()['a']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/self::b')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/self::c')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/self::d')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/self::xxx')], [])

        self.assertEqual([e.value() for e in evaluate(root, '/a/self::(label .)')], [root.value()['a']])  # self:: takes the values inside of its inner expr and uses those values to find matches
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/self::(label .)')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/c/self::(label .)')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/d/self::(label .)')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/self::(label .)')], [])


if __name__ == '__main__':
    unittest.main()
