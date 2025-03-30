import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.pdf.pdf_file_loader import PdfFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = PdfFileLoader().load(
            Path(__file__).parent / 'test.pdf'
        )
        expected = {0: 'Test doc'}

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
