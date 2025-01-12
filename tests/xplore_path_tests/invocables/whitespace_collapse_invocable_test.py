import unittest

from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.invocables.frequency_count_invocable import FrequencyCountInvocable
from xplore_path.invocables.regex_extract_invocable import RegexExtractInvocable
from xplore_path.invocables.whitespace_collapse_invocable import WhitespaceCollapseInvocable
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked(['1 2 3','1   2    3','123'] + PythonObjectPath(None, {'a': 'a a a', 'b': 'b  b b'}).all_children())
        c = WhitespaceCollapseInvocable().invoke([c])
        self.assertEqual(
            list(c.unpack),
            ['a a a', 'b b b', '1 2 3', '1 2 3', '123']
        )


if __name__ == '__main__':
    unittest.main()
