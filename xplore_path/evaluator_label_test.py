import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.dummy.dummy_path import DummyPath
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_extract_labels(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(evaluate(root, 'label //*'), [None, 'a', 'y', 'z', 'ptrs', 'b', 'c', 'd', 'e', 'f', 'd_ptr', 'f_ptr'])

    def test_must_extract_nothing_of_not_paths(self):
        self.assertEqual(evaluate(DummyPath(), 'label (0,1,2,3)'), [])
        self.assertEqual(evaluate(DummyPath(), 'label ()'), [])
        self.assertEqual(evaluate(DummyPath(), 'label 0'), [])
        self.assertEqual(evaluate(DummyPath(), 'label "0"'), [])
        self.assertEqual(evaluate(DummyPath(), 'label "0"'), [])


if __name__ == '__main__':
    unittest.main()
