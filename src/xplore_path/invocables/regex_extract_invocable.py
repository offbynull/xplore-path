import re

from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable


class RegexExtractInvocable(Invocable):
    """
    ```Invocable`` that scans over ``Entity`` values in a ``Collection`` (``Node``\s unpacked to their values) and
    extracts the first occurrence of a regex pattern. The invocation requires exactly 2 arguments:

     1. ``Collection`` to scan over. Non-string values are coerced to string, being silently discarded if coercion is
        not possible.
     2. ``Collection`` containing at least 1 ``Entity``, where the first ``Entity`` is the regex pattern (must be a
        string - not coerced).
    """
    def invoke(self, args: list[Collection]) -> Collection:
        collection, pattern = args
        pattern = next(iter(pattern.unpack))
        collection = collection.transform(lambda _, x: x.coerce(str), DiscardFallbackMode())
        values = list(collection.unpack)
        values = [re.search(pattern, v) for v in values]
        values = [v.group(0) for v in values if v]
        return SequenceCollection.from_unpacked(values)