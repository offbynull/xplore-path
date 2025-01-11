import unittest

from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked(['hello','yellow','miss','miss','brello'] + PythonObjectPath(None, None, 'x', {'a': 'miss', 'b': 'othello'}).all_children())
        c = RegexExtractInvocable().invoke([c, SingleValueCollection('.*el')])
        self.assertEqual(
            list(c.unpack),
            ['othel', 'hel', 'yel', 'brel']
        )


if __name__ == '__main__':
    unittest.main()
