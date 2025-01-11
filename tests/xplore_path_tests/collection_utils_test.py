import unittest

from xplore_path.fallback_modes.error_fallback_mode import ErrorFallbackMode
from xplore_path.collection_utils import combine_transform_aggregate, CombineMode, AggregateMode
from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity


class CollectionTestCase(unittest.TestCase):
    def test_must_combine_single_vs_single(self):
        c1 = SingleValueCollection(1)
        c2 = SingleValueCollection(2)
        c3 = combine_transform_aggregate(c1, c2, CombineMode.ZIP, lambda _, a, __, b: Entity(a.value + b.value), ErrorFallbackMode(), AggregateMode.NONE)
        self.assertIsInstance(c3, SingleValueCollection)
        self.assertEqual(c3.single.value, 3)

    def test_must_combine_single_vs_seq(self):
        c1 = SingleValueCollection(1)
        c2 = SequenceCollection.from_unpacked([2, 3, 4])
        c3 = combine_transform_aggregate(c1, c2, CombineMode.PRODUCT, lambda _, a, __, b: Entity(a.value + b.value), ErrorFallbackMode(), AggregateMode.NONE)
        self.assertIsInstance(c3, SequenceCollection)
        self.assertEqual(list(c3.unpack), [3, 4, 5])

    def test_must_combine_seq_vs_single(self):
        c1 = SequenceCollection.from_unpacked([2, 3, 4])
        c2 = SingleValueCollection(1)
        c3 = combine_transform_aggregate(c1, c2, CombineMode.PRODUCT, lambda _, a, __, b: Entity(a.value + b.value), ErrorFallbackMode(), AggregateMode.NONE)
        self.assertIsInstance(c3, SequenceCollection)
        self.assertEqual(list(c3.unpack), [3, 4, 5])

    def test_must_combine_seq_vs_seq(self):
        c1 = SequenceCollection.from_unpacked([2, 3, 4])
        c2 = SequenceCollection.from_unpacked([1, 2, 3])
        c3 = combine_transform_aggregate(c1, c2, CombineMode.ZIP, lambda _, a, __, b: Entity(a.value + b.value), ErrorFallbackMode(), AggregateMode.NONE)
        self.assertIsInstance(c3, SequenceCollection)
        self.assertEqual(list(c3.unpack), [3, 5, 7])


if __name__ == '__main__':
    unittest.main()
