import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_filter_based_on_position_of_output(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*[1]').unpack], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*[3]').unpack], ['f'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*[5]').unpack], [])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/*[-1]').unpack], [])
        self.assertEqual([e.label() for e in evaluate(root, '/*[0]').unpack], ['a'])
        self.assertEqual([e.label() for e in evaluate(root, '/*[1]').unpack], ['y'])
        self.assertEqual([e.label() for e in evaluate(root, '/*[2]').unpack], ['z'])
        self.assertEqual([e.label() for e in evaluate(root, '/*[3]').unpack], ['ptrs'])
        self.assertEqual([e.label() for e in evaluate(root, '/a[0]/b[0]/*[1]').unpack], ['d'])


if __name__ == '__main__':
    unittest.main()
