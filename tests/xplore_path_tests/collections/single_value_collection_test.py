import unittest

from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode


class TestCase(unittest.TestCase):
    def test_must_transform(self):
        self.assertEqual(list(SingleValueCollection(5).transform(lambda _, x: x, DiscardFallbackMode())), [Entity(5)])
        self.assertEqual(list(SingleValueCollection(5).transform(lambda _, x: None, DiscardFallbackMode())), [])

    def test_must_filter(self):
        self.assertEqual(list(SingleValueCollection(5).filter(lambda _, x: True)), [Entity(5)])
        self.assertEqual(list(SingleValueCollection(5).filter(lambda _, x: False)), [])

    def test_must_maintain_type_when_possible_on_manipulations(self):
        self.assertIsInstance(SingleValueCollection(5).transform(lambda _, x: x, DiscardFallbackMode()), SingleValueCollection)
        self.assertNotIsInstance(SingleValueCollection(5).transform(lambda _, x: None, DiscardFallbackMode()), SingleValueCollection)
        self.assertIsInstance(SingleValueCollection(5).filter(lambda _, x: True), SingleValueCollection)
        self.assertNotIsInstance(SingleValueCollection(5).filter(lambda _, x: False), SingleValueCollection)


if __name__ == '__main__':
    unittest.main()
