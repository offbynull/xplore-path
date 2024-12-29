import unittest
from pathlib import Path

from xplore_path.paths.filesystem.json_file_loader import JsonFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = JsonFileLoader().load(
            Path(__file__).parent / 'test.json'
        )
        expected = {
            "name": "John Doe",
            "age": 30,
            "email": "johndoe@example.com",
            "address": {
                "street": "123 Main Street",
                "city": "Anytown",
                "state": "CA",
                "zip": "12345"
            },
            "phoneNumbers": [
                {
                    "type": "home",
                    "number": "555-555-5555"
                },
                {
                    "type": "work",
                    "number": "555-555-5556"
                }
            ],
            "isEmployed": True,
            "skills": [
                "programming",
                "data analysis",
                "problem solving"
            ]
        }
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
