import unittest
from math import nan, inf

from xplore_path.collection import Collection
from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity
from xplore_path.invocable import Invocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.matchers.strict_matcher import StrictMatcher
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.paths.simple.simple_path import SimplePath


class EntityTestCase(unittest.TestCase):
    def test_must_extract_value(self):
        self.assertEqual(Entity('hi'), 'hi')
        self.assertEqual(Entity(5), 5)
        self.assertEqual(Entity(5.5), 5.5)
        self.assertEqual(Entity(True), True)

    def test_must_pull_out_value_from_path(self):
        self.assertEqual(Entity(PythonObjectPath(None, None, 'hello', 'world')).depath(), 'world')
        self.assertEqual(Entity('world').depath(), 'world')

    def test_must_invoke(self):
        invoke_args = []
        class GoodInvocable(Invocable):
            def invoke(self, args: list[Collection]) -> Collection:
                nonlocal invoke_args
                invoke_args = [a.single for a in args]
                return SingleValueCollection('bye')

        invoke_res = Entity(GoodInvocable()).invoke([SingleValueCollection('hello'), SingleValueCollection('world')])
        invoke_res = invoke_res.single
        self.assertEqual(invoke_args, ['hello', 'world'])
        self.assertEqual(invoke_res, 'bye')

        invoke_args = []
        class BadInvocable(Invocable):
            def invoke(self, args: list[Collection]) -> Collection:
                nonlocal invoke_args
                invoke_args = [a.single for a in args]
                raise ValueError()

        invoke_res = Entity(BadInvocable()).invoke([SingleValueCollection('aa'), SingleValueCollection('bb')])
        self.assertEqual(invoke_args, ['aa', 'bb'])
        self.assertIsNone(invoke_res)
        
    def _coerce_both_test(self, v, t, expected):
        if expected is None:
            self.assertIsNone(Entity(v).coerce(t))
            self.assertIsNone(Entity(SimplePath(None, None, 'fake', v)).coerce(t))
        else:
            self.assertEqual(Entity(v).coerce(t).value, expected)
            self.assertEqual(Entity(SimplePath(None, None, 'fake', v)).coerce(t).value, expected)

    def test_must_coerce_to_bool(self):
        self._coerce_both_test(0, bool, False)
        self._coerce_both_test(5, bool, True)
        self._coerce_both_test(5.5, bool, True)
        self._coerce_both_test(nan, bool, False)
        self._coerce_both_test(inf, bool, True)
        self._coerce_both_test(-inf, bool, True)
        self._coerce_both_test('hi', bool, True)
        self._coerce_both_test('', bool, False)
        self._coerce_both_test(True, bool, True)
        self._coerce_both_test(False, bool, False)
        self._coerce_both_test(StrictMatcher('x'), bool, None)
        self._coerce_both_test(DistinctInvocable(), bool, None)

    def test_must_coerce_to_int(self):
        self._coerce_both_test(0, int, 0)
        self._coerce_both_test(5, int, 5)
        self._coerce_both_test(5.5, int, None)
        self._coerce_both_test(nan, int, None)
        self._coerce_both_test(inf, int, None)
        self._coerce_both_test(-inf, int, None)
        self._coerce_both_test('hi', int, None)
        self._coerce_both_test('5', int, 5)
        self._coerce_both_test('', int, None)
        self._coerce_both_test(True, int, 1)
        self._coerce_both_test(False, int, 0)
        self._coerce_both_test(StrictMatcher('x'), int, None)
        self._coerce_both_test(DistinctInvocable(), int, None)
        
    def test_must_coerce_to_float(self):
        self._coerce_both_test(0, float, 0.0)
        self._coerce_both_test(5, float, 5.0)
        self._coerce_both_test(5.5, float, 5.5)
        # self._coerce_both_test(nan, float, nan)  # should pass but nan == nan is never true
        self._coerce_both_test(inf, float, inf)
        self._coerce_both_test(-inf, float, -inf)
        self._coerce_both_test('hi', float, None)
        self._coerce_both_test('5', float, 5.0)
        self._coerce_both_test('', float, None)
        self._coerce_both_test(True, float, 1.0)
        self._coerce_both_test(False, float, 0.0)
        self._coerce_both_test(StrictMatcher('x'), float, None)
        self._coerce_both_test(DistinctInvocable(), float, None)
        
    def test_must_coerce_to_str(self):
        self._coerce_both_test(0, str, '0')
        self._coerce_both_test(5, str, '5')
        self._coerce_both_test(5.5, str, '5.5')
        self._coerce_both_test(nan, str, 'nan')
        self._coerce_both_test(inf, str, 'inf')
        self._coerce_both_test(-inf, str, '-inf')
        self._coerce_both_test('hi', str, 'hi')
        self._coerce_both_test('', str, '')
        self._coerce_both_test(True, str, 'True')
        self._coerce_both_test(False, str, 'False')
        # self._coerce_both_test(StrictMatcher('x'), str, 'xxx')  # converts but not deterministic
        # self._coerce_both_test(DistinctInvocable(), str, 'xxx')  # converts but not deterministic

    def test_must_coerce_to_matching(self):
        e1, e2 = Entity.coerce_to_matching(Entity('5'), Entity(4))
        self.assertEqual(e1.value, '5')
        self.assertEqual(e2.value, '4')
        e1, e2 = Entity.coerce_to_matching(Entity(5), Entity('4'))
        self.assertEqual(e1.value, 5)
        self.assertEqual(e2.value, 4)
        e1, e2 = Entity.coerce_to_matching(Entity(5), Entity('x'))
        self.assertEqual(e1.value, '5')
        self.assertEqual(e2.value, 'x')
        e1, e2 = Entity.coerce_to_matching(Entity(5), Entity(StrictMatcher('x')))
        self.assertIsNone(e1)
        self.assertIsNone(e2)


if __name__ == '__main__':
    unittest.main()
