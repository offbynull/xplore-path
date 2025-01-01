import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual(
            [e.value() for e in evaluate(root, '/a/descendant::f')],
            [root.value()['a']['b']['f']]
        )
        self.assertEqual(
            [e.value() for e in evaluate(root, '/a/descendant::(label .)')],
            [
                root.value()['a']['b'],
                root.value()['a']['b']['c'],
                root.value()['a']['b']['d'],
                root.value()['a']['b']['e'],
                root.value()['a']['b']['f']
            ]
        )
        self.assertEqual(
            [e.value() for e in evaluate(root, '/a/descendant::*')],
            [e.value() for e in evaluate(root, '/a//*')]
        )
        self.assertEqual(
            [e.value() for e in evaluate(root, '/a/descendant::(label .)')],
            [e.value() for e in evaluate(root, '/a//*')]
        )
        self.assertEqual(
            sorted([e.value() for e in evaluate(root, '/descendant::*')], key=id),
            sorted([e.value() for e in evaluate(root, '//*')], key= id)
        )


if __name__ == '__main__':
    unittest.main()
