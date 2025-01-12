import unittest

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.invocables.count_invocable import CountInvocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked([1,2,3,4,5] + PythonObjectPath(None, {'a': 5, 'b': 6}).all_children())
        self.assertEqual(set(DistinctInvocable().invoke([c]).unpack), {1,2,3,4,5,6})


if __name__ == '__main__':
    unittest.main()
