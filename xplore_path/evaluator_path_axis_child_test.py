import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_walk_to_child_using_child_directive(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.value() for e in evaluate(root, '/a/child::b')], [root.value()['a']['b']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/child::c')], [root.value()['a']['b']['c']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/child::d')], [root.value()['a']['b']['d']])
        self.assertEqual([e.value() for e in evaluate(root, '/ptrs/child::d_ptr')], [root.value()['ptrs']['d_ptr']])
        self.assertEqual([e.value() for e in evaluate(root, '/ptrs/child::f_ptr')], [root.value()['ptrs']['f_ptr']])
        self.assertEqual([e.value() for e in evaluate(root, '/a/b/xxx/child::xxx')], [])

        self.assertEqual(
            [e.value() for e in evaluate(root, '/a/b/child::(label .)')],
            [
                root.value()['a']['b']['c'],
                root.value()['a']['b']['d'],
                root.value()['a']['b']['e'],
                root.value()['a']['b']['f']
            ]
        )


if __name__ == '__main__':
    unittest.main()
