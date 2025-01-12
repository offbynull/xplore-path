import unittest
from pathlib import Path

from xplore_path.paths.filesystem.file_loaders.sqlite.sqlite_file_loader import SqliteFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        fs_path = Path(__file__).parent / 'test.sqlite'
        raw_data = SqliteFileLoader().load(fs_path)
        path_creator = SqliteFileLoader().path_creator(fs_path)
        path = path_creator(None, raw_data)
        # for inner_path in path.all_descendants(max_level=6):
        #     print(f'{inner_path}')
        self.assertEqual(42, len(path.all_descendants()))  # too lazy to write out every assertion


if __name__ == '__main__':
    unittest.main()
