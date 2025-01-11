import unittest

from xplore_path.evaluator import evaluate
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class EvaluatorTest(unittest.TestCase):
    def test_must_treat_part_after_directive_as_expression_executed_within_context_of_each_path_returned(self):
        root = PythonObjectPath.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': -2}}, 'y': 3, 'z': 4, 'ptrs': {'d_ptr': 'd', 'f_ptr': 'f'}})
        self.assertEqual([e.label() for e in evaluate(root, '/a/child::b').unpack], ['b'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/child::c').unpack], ['c'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/child::d').unpack], ['d'])
        self.assertEqual([e.label() for e in evaluate(root, '/ptrs/child::d_ptr').unpack], ['d_ptr'])
        self.assertEqual([e.label() for e in evaluate(root, '/ptrs/child::f_ptr').unpack], ['f_ptr'])
        self.assertEqual([e.label() for e in evaluate(root, '/a/b/xxx/child::xxx').unpack], [])

        self.assertEqual(
            [e.label() for e in evaluate(root, '/a/b/child::(label .)').unpack],
            ['c','d','e','f']
        )


if __name__ == '__main__':
    unittest.main()
