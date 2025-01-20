from typing import Hashable

from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable
from xplore_path.null import Null


class DistinctInvocable(Invocable):
    """
    ```Invocable`` that returns the distinct ``Entity`` values in a ``Collection`` (``Node``\s unpacked to their
    values). Unhashable values are silently discarded.
    """
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        result = result.transform(lambda _, e: e.denode(), DiscardFallbackMode())
        result = result.filter_unpacked(lambda _, v: isinstance(v, Hashable))
        return SequenceCollection.from_unpacked(set(result.unpack))  # noqa