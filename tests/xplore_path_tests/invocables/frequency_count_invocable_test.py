import unittest

from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked([1,2,3,4,5] + PythonObjectPath(None, None, 'x', {'a': 5, 'b': 6}).all_children())
        c = FrequencyCountInvocable().invoke([c])
        c = list(c.unpack)
        self.assertEqual(len(c), 1)
        self.assertEqual(
            c[0].to_dict(),
            {
                1: (1, {}),
                2: (1, {}),
                3: (1, {}),
                4: (1, {}),
                5: (2, {}),
                6: (1, {})
            }
        )


if __name__ == '__main__':
    unittest.main()
