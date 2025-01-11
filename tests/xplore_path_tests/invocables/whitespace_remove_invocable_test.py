import unittest

from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.invocables.whitespace_remove_invocable import WhitespaceRemoveInvocable
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_invoke(self):
        c = SequenceCollection.from_unpacked(['1 2 3','1   2    3','123'] + PythonObjectPath(None, None, 'x', {'a': 'a a a', 'b': 'b  b b'}).all_children())
        c = WhitespaceRemoveInvocable().invoke([c])
        self.assertEqual(
            list(c.unpack),
            ['aaa', 'bbb', '123', '123', '123']
        )


if __name__ == '__main__':
    unittest.main()
