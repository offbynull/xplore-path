import pathlib
import shutil
import tempfile
import unittest

from xplore_path.paths.filesystem.filesystem_path import FileSystemPath, FileSystemPathContext


class TestCase(unittest.TestCase):
    def test_filesystem_access(self):
        with tempfile.TemporaryDirectory() as files_dir, tempfile.TemporaryDirectory() as workspace_dir:
            # copy to tempdir
            files_dir_path = pathlib.Path(files_dir)
            current_path = pathlib.Path(__file__).parent
            files_to_copy = current_path.glob("**/test.*")
            for file_path in files_to_copy:
                shutil.copy(file_path, files_dir_path)
            # create
            workspace_dir_path = pathlib.Path(workspace_dir)
            fsp = FileSystemPath(
                None,
                None,
                None,
                files_dir_path,
                FileSystemPathContext(
                    workspace=workspace_dir_path
                )
            )
            # walk
            fsp_descendants = fsp.all_descendants()
        self.assertEqual(185, len(fsp_descendants))  # just check length - too lazy to check everything


if __name__ == '__main__':
    unittest.main()
