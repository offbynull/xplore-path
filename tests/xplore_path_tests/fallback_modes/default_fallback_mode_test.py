import unittest

from xplore_path.fallback_modes.default_fallback_mode import DefaultFallbackMode


class TestCase(unittest.TestCase):
    def test_must_evaluate(self):
        self.assertEqual(DefaultFallbackMode('x').evaluate(0), (0, ))
        self.assertEqual(DefaultFallbackMode('x').evaluate(1), (1, ))
        self.assertEqual(DefaultFallbackMode('x').evaluate(None), ('x', ))

if __name__ == '__main__':
    unittest.main()
