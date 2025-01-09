import unittest
from pathlib import Path

from xplore_path.paths.filesystem.file_loaders.csv.csv_file_loader import CsvFileLoader
from xplore_path.paths.filesystem.file_loaders.tsv.tsv_file_loader import TsvFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = TsvFileLoader().load(
            Path(__file__).parent / 'test.tsv'
        )
        expected = {
            0: {'h1': 'a', 'h2': 'b', 'h3': 'c'},
            1: {'h1': 'd', 'h2': 'e', 'h3': 'f'}
        }

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
