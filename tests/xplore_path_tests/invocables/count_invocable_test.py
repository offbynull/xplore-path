import unittest

from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.invocables.count_invocable import CountInvocable


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked([1,2,3,4,5])
        self.assertEqual(CountInvocable().invoke([c]).single, 5)
        c = SequenceCollection.empty()
        self.assertEqual(CountInvocable().invoke([c]).single, 0)


if __name__ == '__main__':
    unittest.main()
