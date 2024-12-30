import pathlib
import unittest

from xplore_path.paths.filesystem.filesystem_path import FileSystemPath, FileSystemPathContext


class TestCase(unittest.TestCase):
    def test_something(self):
        fsp = FileSystemPath(
            None,
            None,
            pathlib.Path(__file__).parent,
            FileSystemPathContext(
                workspace=
            )
        )
        self.assertEqual(True, False)  # add assertion here

if __name__ == '__main__':
    unittest.main()
