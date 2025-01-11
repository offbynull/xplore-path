from typing import Hashable

from xplore_path.collection import Collection
from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.invocable import Invocable


class DistinctInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        return SequenceCollection.from_unpacked({e.depath().value for e in result if isinstance(e.depath().value, Hashable)})