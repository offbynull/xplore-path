import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from xplore_path.nodes.filesystem.cache import Cache


class TestCacheCase(unittest.TestCase):
    def test_must_cache_and_load(self):
        with TemporaryDirectory(delete=True) as d:
            cache = Cache(Path(f'{d}/xplore_path_cache'), 1)
            self.assertEqual(cache.load('missing-key'), (False, None))
            cache.cache('key1', 'hi')
            cache.cache('key2', 'bye')
            cache.cache('key3', [1, 2, 3, 4])
            self.assertEqual(cache.load('key1'), (True, 'hi'))
            self.assertEqual(cache.load('key2'), (True, 'bye'))
            self.assertEqual(cache.load('key3'), (True, [1, 2, 3, 4]))
            cache.cache('key3', 'overridden')
            self.assertEqual(cache.load('key3'), (True, 'overridden'))
            self.assertEqual(cache.load('key1'), (True, 'hi'))
            self.assertEqual(cache.load('key2'), (True, 'bye'))
            self.assertEqual(cache.load('key3'), (True, 'overridden'))
            self.assertEqual(cache.load('missing-key'), (False, None))


if __name__ == '__main__':
    unittest.main()
