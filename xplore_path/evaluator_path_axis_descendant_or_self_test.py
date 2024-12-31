import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_walk_to_descendants(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        # self.assertEqual(
        #     [e.value() for e in evaluate(root, '/a/descendant-or-self::f')],
        #     [root.value()['a']['b']['f']]
        # )
        self.assertEqual(
            sorted([e.full_label() for e in evaluate(root, '/a//descendant-or-self::(label .)')]),  THIS IS RETURNING DUPLICATES? FIX IT
            sorted([e.full_label() for e in evaluate(root, '/a')] + [e.full_label() for e in evaluate(root, '/a//*')])
        )


if __name__ == '__main__':
    unittest.main()
