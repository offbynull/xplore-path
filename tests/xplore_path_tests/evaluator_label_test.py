import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.dummy.dummy_node import DummyNode
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_must_extract_labels(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(evaluate(root, 'label //*'), ['a', 'b', 'c', 'd', 'e', 'f', 'y', 'z', 'ptrs', 'd_ptr', 'f_ptr'])

    def test_must_extract_nothing_of_not_paths(self):
        self.assertEqual(evaluate(DummyNode(), 'label (0,1,2,3)'), [])
        self.assertEqual(evaluate(DummyNode(), 'label ()'), [])
        self.assertEqual(evaluate(DummyNode(), 'label 0'), [])
        self.assertEqual(evaluate(DummyNode(), 'label "0"'), [])
        self.assertEqual(evaluate(DummyNode(), 'label "0"'), [])


if __name__ == '__main__':
    unittest.main()
