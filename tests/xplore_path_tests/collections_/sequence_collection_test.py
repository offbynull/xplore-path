import itertools
import unittest
from random import Random

from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.entity import Entity
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


class TestCase(unittest.TestCase):
    def test_must_transform(self):
        self.assertEqual(list(SequenceCollection.from_unpacked([5, 4, 3]).transform(lambda _, x: Entity(x.value+1), DiscardFallbackMode()).unpack), [6, 5, 4])
        self.assertEqual(list(SequenceCollection.from_unpacked([5, 4, 3]).transform(lambda _, x: None, DiscardFallbackMode()).unpack), [])

    def test_must_filter(self):
        self.assertEqual(list(SequenceCollection.from_unpacked([5, 4, 3]).filter(lambda _, x: x.value >= 4).unpack), [5, 4])

    def test_must_order(self):
        paths = PythonObjectNode(None, {'a': ['b', 'c'], 'd': 5, 'e': 3}).descendants()
        randomized_paths = paths[:]
        Random(0).shuffle(randomized_paths)
        randomized_values = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        Random(0).shuffle(randomized_values)
        self.assertEqual(
            list(
                SequenceCollection.from_unpacked(
                    randomized_paths + randomized_values + randomized_paths,
                    order_paths=True,
                    deduplicate_paths=False
                ).unpack
            ),
            list(itertools.chain(*([p, p] for p in paths))) + randomized_values
        )

    def test_must_dedupe(self):
        paths = PythonObjectNode(None, {'a': ['b', 'c'], 'd': 5, 'e': 3}).descendants()
        randomized_paths = paths[:]
        Random(0).shuffle(randomized_paths)
        randomized_values = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        Random(0).shuffle(randomized_values)
        self.assertEqual(
            list(
                SequenceCollection.from_unpacked(
                    randomized_paths + randomized_values + randomized_paths,
                    order_paths=False,
                    deduplicate_paths=True
                ).unpack
            ),
            randomized_paths + randomized_values
        )

    def test_must_order_and_dedupe(self):
        paths = PythonObjectNode(None, {'a': ['b', 'c'], 'd': 5, 'e': 3}).descendants()
        randomized_paths = paths[:]
        Random(0).shuffle(randomized_paths)
        randomized_values = [5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
        Random(0).shuffle(randomized_values)
        self.assertEqual(
            list(
                SequenceCollection.from_unpacked(
                    randomized_paths + randomized_values + randomized_paths,
                    order_paths=True,
                    deduplicate_paths=True
                ).unpack
            ),
            paths + randomized_values
        )


if __name__ == '__main__':
    unittest.main()
