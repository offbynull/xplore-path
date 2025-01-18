import unittest

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.collections_.single_value_collection import SingleValueCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked(['hello','yellow','miss','miss','brello'] + PythonObjectNode(None, {'a': 'miss', 'b': 'othello'}).children())
        c = RegexExtractInvocable().invoke([c, SingleValueCollection('.*el')])
        self.assertEqual(
            list(c.unpack),
            ['othel', 'hel', 'yel', 'brel']
        )


if __name__ == '__main__':
    unittest.main()
