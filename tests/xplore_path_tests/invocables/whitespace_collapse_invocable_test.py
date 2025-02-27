import unittest

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.collections_.single_value_collection import SingleValueCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked(['1 2 3','1   2    3','123'] + PythonObjectNode(None, {'a': 'a a a', 'b': 'b  b b'}).children())
        c = WhitespaceCollapseInvocable().invoke([c])
        self.assertEqual(
            list(c.unpack),
            ['a a a', 'b b b', '1 2 3', '1 2 3', '123']
        )


if __name__ == '__main__':
    unittest.main()
