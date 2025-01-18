import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.docx.docx_file_loader import DocxFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = DocxFileLoader().load(
            Path(__file__).parent / 'test.docx'
        )
        expected = 'Test doc'

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
