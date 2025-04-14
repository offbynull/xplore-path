import unittest

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


def evaluate(root, expr, variables = None):
    return Evaluator(variables).evaluate(root, expr)


class EvaluatorTest(unittest.TestCase):
    def test_fix_for_and_failure(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': {'g': -2, 'h': -3}}, 'y': 3, 'z': 4, 'u': {'t': 4}, 'v': {}}})
        # Regression test: Grammar ambiguity was causing the query below to fail
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=-3 and ../y=3]').unpack).label(), 'b')
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=-3 and ../y=3 and ../z]').unpack).label(), 'b')
        # Regression test: ../u must evaluate to True - it's not empty
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=-3 and ../u]').unpack).label(), 'b')
        # Regression test: ../v/* must evaluate to False - it's empty
        self.assertEqual(evaluate(root, '/a/b[./f/h=-3 and ../v/*]'), [])

    def test_fix_for_or_failure(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': {'g': -2, 'h': -3}}, 'y': 3, 'z': 4, 'u': {'t': 4}, 'v': {}}})
        # Regression test: Grammar ambiguity was causing the query below to fail
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=55 or ../y=3]').unpack).label(), 'b')
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=55 or ../y=55 or ../z]').unpack).label(), 'b')
        # Regression test: ../u must evaluate to True - it's not empty
        self.assertEqual(next(evaluate(root, '/a/b[./f/h=55 or ../u]').unpack).label(), 'b')
        # Regression test: ../v/* must evaluate to False - it's empty
        self.assertEqual(evaluate(root, '/a/b[./f/h=55 or ../v/*]'), [])

    def test_fix_for_and_or_where_operand_contains_all_any(self):
        root = PythonObjectNode.create_root_path({'a': {'b': {'c': 1, 'd': 2, 'e': -1, 'f': {'g': -2, 'h': -3}}, 'y': 3, 'z': 4, 'u': {'t': 4}, 'v': {}}})
        # Regression test: These would all cause a crash.
        self.assertEqual(next(evaluate(root, '/a[./b/f/h=55 or all(./u/*)]').unpack).label(), 'a')
        self.assertEqual(next(evaluate(root, '/a[./b/f/h=55 or any(./u/*)]').unpack).label(), 'a')
        self.assertEqual(next(evaluate(root, '/a[./b/f/h=-3 and all(./u/*)]').unpack).label(), 'a')
        self.assertEqual(next(evaluate(root, '/a[./b/f/h=-3 and any(./u/*)]').unpack).label(), 'a')