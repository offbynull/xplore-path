import unittest

from xplore_path.fallback_modes.error_fallback_mode import ErrorFallbackMode


class TestCase(unittest.TestCase):
    def test_must_evaluate(self):
        self.assertEqual(ErrorFallbackMode().evaluate(0), (0, ))
        self.assertEqual(ErrorFallbackMode().evaluate(1), (1, ))
        with self.assertRaises(ValueError):
            ErrorFallbackMode().evaluate(None)

if __name__ == '__main__':
    unittest.main()
