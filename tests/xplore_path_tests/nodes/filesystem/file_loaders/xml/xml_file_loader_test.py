import unittest
from pathlib import Path

from xplore_path.nodes.filesystem.file_loaders.xml.xml_file_loader import XmlFileLoader
from xplore_path.nodes.filesystem.file_loaders.xml.xml_object_node import XmlTag


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = XmlFileLoader().load(
            Path(__file__).parent / 'test.xml'
        )
        expected = XmlTag(name='catalog', attrs={}, text=None, values=[
            XmlTag(name='book', attrs={'@id': 'bk101'}, text=None, values=[
                XmlTag(name='title', attrs={}, text="XML Developer's Guide", values=[]),
                XmlTag(name='author', attrs={}, text='Gambardella, Matthew', values=[]),
                XmlTag(name='genre', attrs={}, text='Computer', values=[]),
                XmlTag(name='price', attrs={}, text='44.95', values=[]),
                XmlTag(name='publish_date', attrs={}, text='2000-10-01', values=[]),
                XmlTag(name='description', attrs={}, text='An in-depth look at creating applications with XML.', values=[])
            ]),
            XmlTag(name='book', attrs={'@id': 'bk102'}, text=None, values=[
                XmlTag(name='title', attrs={}, text='Midnight Rain', values=[]),
                XmlTag(name='author', attrs={}, text='Ralls, Kim', values=[]),
                XmlTag(name='genre', attrs={}, text='Fantasy', values=[]),
                XmlTag(name='price', attrs={}, text='5.95', values=[]),
                XmlTag(name='publish_date', attrs={}, text='2000-12-16', values=[]),
                XmlTag(name='description', attrs={}, text='A former architect battles corporate zombies,\n        an evil sorceress, and her own childhood to become queen\n        of the world.', values=[])
            ]),
            XmlTag(name='book', attrs={'@id': 'bk103'}, text=None, values=[
                XmlTag(name='title', attrs={}, text='Maeve Ascendant', values=[]),
                XmlTag(name='author', attrs={}, text='Corets, Eva', values=[]),
                XmlTag(name='genre', attrs={}, text='Fantasy', values=[]),
                XmlTag(name='price', attrs={}, text='5.95', values=[]),
                XmlTag(name='publish_date', attrs={}, text='2000-11-17', values=[]),
                XmlTag(name='description', attrs={}, text='After the collapse of a nanotechnology\n        society in England, the young survivors lay the\n        foundation for a new society.', values=[])
            ])
        ])
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
