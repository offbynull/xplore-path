import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.csv.csv_file_loader import CsvFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = CsvFileLoader().load(
            Path(__file__).parent / 'test.csv'
        )
        expected = {
            0: {'h1': 'a', 'h2': 'b', 'h3': 'c'},
            1: {'h1': 'd', 'h2': 'e', 'h3': 'f'}
        }

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
