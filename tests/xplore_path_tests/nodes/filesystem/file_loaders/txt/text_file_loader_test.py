import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.txt.text_file_loader import TextFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = TextFileLoader().load(
            Path(__file__).parent / 'test.txt'
        )
        expected = {'content': 'hello world!'}

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
