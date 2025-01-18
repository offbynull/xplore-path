import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/a/self::a').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/self::b').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/self::c').unpack], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d/self::d').unpack], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/self::xxx').unpack], [])

        self.assertEqual([e.label() for e in evaluate(root, '/a/self::(label .)').unpack], ['a'])  # self:: takes the values inside of its inner expr and uses those values to find matches
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/self::(label .)').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/c/self::(label .)').unpack], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/d/self::(label .)').unpack], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/self::(label .)').unpack], [])


if __name__ == '__main__':
    unittest.main()
