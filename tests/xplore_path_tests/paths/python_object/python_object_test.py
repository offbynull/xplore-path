import unittest

from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class TestCase(unittest.TestCase):
    def test_must_list_appropriate_number_of_descendants(self):
        p = PythonObjectPath(None, None, None, {'a': {'b': ['c', 'd', 'e', 'f']}, 'y': {3, 4}, 'z': (5, 6)})
        self.assertEqual(3, len(p.all_children()))  # sanity check
        self.assertEqual(11, len(p.all_descendants()))  # sanity check


if __name__ == '__main__':
    unittest.main()
