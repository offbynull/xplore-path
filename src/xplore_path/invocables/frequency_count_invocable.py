from collections import Counter
from typing import Hashable

from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable
from xplore_path.null import Null
from xplore_path.node import Node
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode
from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection


class FrequencyCountInvocable(Invocable):
    """
    ```Invocable`` that counts the number of times each distinct ``Entity`` value in a ``Collection`` occurs (``Node``\s
    unpacked to their values). Unhashable values are silently discarded.
    """
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        result = result.transform(lambda _, e: e.denode(), DiscardFallbackMode())
        result = result.filter_unpacked(lambda _, v: isinstance(v, Hashable))
        counter = Counter(v for v in result.unpack)
        output = {value: count for value, count in counter.most_common()}
        return SequenceCollection.from_unpacked(
            [PythonObjectNode(None, output)],
            order_nodes=False,
            deduplicate_nodes=False
        )