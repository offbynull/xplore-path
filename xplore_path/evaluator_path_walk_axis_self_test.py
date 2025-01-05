import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/a/self::a')], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/self::b')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/self::c')], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d/self::d')], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/self::xxx')], [])

        self.assertEqual([e.label() for e in evaluate(root, '/a/self::(label .)')], ['a'])  # self:: takes the values inside of its inner expr and uses those values to find matches
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/self::(label .)')], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/self::(label .)')], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d/self::(label .)')], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/self::(label .)')], [])


if __name__ == '__main__':
    unittest.main()
