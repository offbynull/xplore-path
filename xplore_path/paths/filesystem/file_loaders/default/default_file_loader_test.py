import unittest
from pathlib import Path

from xplore_path.paths.filesystem.file_loaders.default.default_file_loader import DefaultFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = DefaultFileLoader().load(
            Path(__file__).parent / 'test.txt'
        )
        expected = 'hello world!'
        self.assertEqual(expected, actual)

        actual = DefaultFileLoader().load(
            Path(__file__).parent / 'NON_EXISTANT_FILE'
        )
        expected = []
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
