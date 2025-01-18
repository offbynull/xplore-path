import unittest

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.invocables.count_invocable import CountInvocable
from xplore_path.invocables.distinct_invocable import DistinctInvocable
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked([1,2,3,4,5] + PythonObjectNode(None, {'a': 5, 'b': 6}).children())
        self.assertEqual(set(DistinctInvocable().invoke([c]).unpack), {1,2,3,4,5,6})


if __name__ == '__main__':
    unittest.main()
