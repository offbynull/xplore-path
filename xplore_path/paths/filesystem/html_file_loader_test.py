import unittest
from pathlib import Path

from xplore_path.paths.filesystem.html_file_loader import HtmlFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = HtmlFileLoader().load(
            Path(__file__).parent / 'test.html'
        )
        expected = {
            'html': {
                1: {'head': {1: {'title': {0: 'Example HTML'}}}},
                3: {'body': {
                    1: {'h1': {0: 'Hello, World!'}},
                    3: {'p': {0: 'This is a paragraph.'}},
                    5: {'div': {0: 'A div'}},
                    7: {'p': {0: 'Another paragraph'}},
                    9: {'a': {'@href': 'https://example.com', 0: 'Example Link'}}
                }}
            }
        }


        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
