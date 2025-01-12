from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable


class WhitespaceStripInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        collection, = args
        collection = collection.transform(lambda _, x: x.coerce(str), DiscardFallbackMode())
        values = list(collection.unpack)
        return SequenceCollection.from_unpacked(v.strip() for v in values)