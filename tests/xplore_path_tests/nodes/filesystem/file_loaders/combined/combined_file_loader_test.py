import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.combined.combined_file_loader import CombinedFileLoader
from xplore_path.nodes.filesystem.file_loaders.docx.docx_file_loader import DocxFileLoader
from xplore_path.nodes.filesystem.file_loaders.json.json_file_loader import JsonFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        loader = CombinedFileLoader([
            DocxFileLoader(),
            JsonFileLoader()
        ])
        actual = loader.load(Path(__file__).parent.parent / 'docx' / 'test.docx')
        expected = 'Test doc'
        self.assertEqual(expected, actual)
        actual = loader.load(Path(__file__).parent.parent / 'json' / 'test.json')
        expected = 'John Doe'
        self.assertEqual(expected, actual['name'])  # good enough to test for a field in the JSON, not the entire JSON
        actual = loader.load(Path(__file__).parent / 'NON_EXISTANT')
        self.assertIsNone(actual)


if __name__ == '__main__':
    unittest.main()
