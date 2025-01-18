import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.html.html_file_loader import HtmlFileLoader
from xplore_path.nodes.filesystem.file_loaders.xml.xml_object_node import XmlTag


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = HtmlFileLoader().load(
            Path(__file__).parent / 'test.html'
        )
        print(f'{actual}')
        expected = XmlTag(name='html', attrs={}, text=None, values=[
            XmlTag(name='head', attrs={}, text=None, values=[
                XmlTag(name='title', attrs={}, text='Example HTML', values=[])
            ]),
            XmlTag(name='body', attrs={}, text=None, values=[
                XmlTag(name='h1', attrs={}, text='Hello, World!', values=[]),
                XmlTag(name='p', attrs={}, text='This is a paragraph.', values=[]),
                XmlTag(name='div', attrs={}, text='A div', values=[]),
                XmlTag(name='p', attrs={}, text='Another paragraph', values=[]),
                XmlTag(name='a', attrs={'@href': 'https://example.com'}, text='Example Link', values=[])
            ])
        ])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
