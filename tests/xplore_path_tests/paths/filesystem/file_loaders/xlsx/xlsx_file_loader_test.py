import unittest
from pathlib import Path

from xplore_path.paths.filesystem.file_loaders.xlsx.xlsx_file_loader import XlsxFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = XlsxFileLoader().load(
            Path(__file__).parent / 'test.xlsx'
        )
        expected = {
            'Sheet1': {
                0: {'h1': 'a', 'h2': 'b', 'h3': 'c'},
                1: {'h1': 'd', 'h2': 'e', 'h3': 'f'}
            }
        }

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
