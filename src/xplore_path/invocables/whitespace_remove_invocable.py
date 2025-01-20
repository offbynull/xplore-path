import re

from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable


class WhitespaceRemoveInvocable(Invocable):
    """
    ```Invocable`` that scans over ``Entity`` values in a ``Collection`` (``Node``\s unpacked to their values) and
    removes all whitespace. Non-string values are coerced to string, being silently discarded if coercion is not
    possible.
    """
    def invoke(self, args: list[Collection]) -> Collection:
        collection, = args
        collection = collection.transform(lambda _, x: x.coerce(str), DiscardFallbackMode())
        values = list(collection.unpack)
        return SequenceCollection.from_unpacked(re.sub(r'\s+', '', v) for v in values)