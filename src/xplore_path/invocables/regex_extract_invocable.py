import re

from xplore_path.collection import Collection
from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable


class RegexExtractInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        collection, pattern = args
        pattern = next(iter(pattern.unpack))
        collection = collection.transform(lambda _, x: x.coerce(str), DiscardFallbackMode())
        values = list(collection.unpack)
        values = [re.search(pattern, v) for v in values]
        values = [v.group(0) for v in values if v]
        return SequenceCollection.from_unpacked(values)