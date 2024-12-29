import unittest
from pathlib import Path

from xplore_path.paths.filesystem.xml_file_loader import XmlFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = XmlFileLoader().load(
            Path(__file__).parent / 'test.xml'
        )
        expected = {
            'catalog': {
                0: {
                    'book': {
                        '@id': 'bk101',
                        0: {'title': {'.text': "XML Developer's Guide"}},
                        1: {'author': {'.text': 'Gambardella, Matthew'}},
                        2: {'genre': {'.text': 'Computer'}},
                        3: {'price': {'.text': '44.95'}},
                        4: {'publish_date': {'.text': '2000-10-01'}},
                        5: {'description': {'.text': 'An in-depth look at creating applications with XML.'}}
                    }
                },
                1: {
                    'book': {
                        '@id': 'bk102',
                        0: {'title': {'.text': 'Midnight Rain'}},
                        1: {'author': {'.text': 'Ralls, Kim'}},
                        2: {'genre': {'.text': 'Fantasy'}},
                        3: {'price': {'.text': '5.95'}},
                        4: {'publish_date': {'.text': '2000-12-16'}},
                        5: {'description': {'.text': 'A former architect battles corporate zombies,\n        an evil sorceress, and her own childhood to become queen\n        of the world.'}}
                    }
                },
                2: {
                    'book': {
                        '@id': 'bk103',
                        0: {'title': {'.text': 'Maeve Ascendant'}},
                        1: {'author': {'.text': 'Corets, Eva'}},
                        2: {'genre': {'.text': 'Fantasy'}},
                        3: {'price': {'.text': '5.95'}},
                        4: {'publish_date': {'.text': '2000-11-17'}},
                        5: {'description': {'.text': 'After the collapse of a nanotechnology\n        society in England, the young survivors lay the\n        foundation for a new society.'}}}
                }
            }
        }

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
