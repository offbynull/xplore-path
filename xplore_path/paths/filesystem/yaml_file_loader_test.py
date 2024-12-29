import unittest
from pathlib import Path

from xplore_path.paths.filesystem.yaml_file_loader import YamlFileLoader


class TestCase(unittest.TestCase):
    def test_must_load_example_sanity_test(self):
        actual = YamlFileLoader().load(
            Path(__file__).parent / 'test.yaml'
        )
        expected = {
            'person': {
                'name': 'John Doe',
                'age': 30,
                'occupation': 'Software Engineer',
                'skills': ['Python', 'JavaScript', 'Cloud Computing'],
                'hobbies': {
                    'outdoor': ['hiking', 'cycling'],
                    'indoor': ['reading', 'gaming']
                },
                'contact_info': {'email': 'john.doe@example.com', 'phone': '+1234567890'},
                'address': {'street': '123 Main St', 'city': 'Metropolis', 'state': 'CA', 'zip_code': '12345'}
            }
        }
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
