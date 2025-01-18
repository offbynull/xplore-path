import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_evaluate_to_self(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(list(evaluate(root, '.').unpack), [root])
        self.assertEqual(list(evaluate(root, '/').unpack), [root])
        self.assertEqual(list(evaluate(root, '/.').unpack), [root])
        self.assertEqual(list(evaluate(root, '.').unpack), [root])

    def test_must_walk_to_self_using_dot(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/.').unpack], [['a']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/.').unpack], [['a', 'b']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/c/.').unpack], [['a', 'b', 'c']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/d/.').unpack], [['a', 'b', 'd']])
        self.assertEqual([e.full_label() for e in evaluate(root, '/a/b/xxx/.').unpack], [])


if __name__ == '__main__':
    unittest.main()
