import unittest

from xplore_path.fallback_modes.default_fallback_mode import DefaultFallbackMode
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode


class TestCase(unittest.TestCase):
    def test_must_evaluate(self):
        self.assertEqual(DiscardFallbackMode().evaluate(0), (0, ))
        self.assertEqual(DiscardFallbackMode().evaluate(1), (1, ))
        self.assertEqual(DiscardFallbackMode().evaluate(None), ())

if __name__ == '__main__':
    unittest.main()
