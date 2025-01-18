import unittest

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.collections_.single_value_collection import SingleValueCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.invocables.whitespace_strip_invocable import WhitespaceStripInvocable
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked([' 1 2 3','123 ',' 123 '] + PythonObjectNode(None, {'a': ' aa a', 'b': 'bb b '}).children())
        c = WhitespaceStripInvocable().invoke([c])
        self.assertEqual(
            list(c.unpack),
            ['aa a', 'bb b', '1 2 3', '123', '123']
        )


if __name__ == '__main__':
    unittest.main()
