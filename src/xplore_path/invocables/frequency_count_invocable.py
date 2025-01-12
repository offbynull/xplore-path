from collections import Counter
from typing import Hashable

from xplore_path.fallback_modes.discard_fallback_mode import DiscardFallbackMode
from xplore_path.invocable import Invocable
from xplore_path.null import Null
from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.collection import Collection
from xplore_path.collections_.sequence_collection import SequenceCollection


class FrequencyCountInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        result = result.transform(lambda _, e: e.depath(), DiscardFallbackMode())# = [v.value() if isinstance(v, Path) else v for v in result.unpack]
        result = result.filter_unpacked(lambda _, v: isinstance(v, Hashable))
        counter = Counter(v for v in result.unpack)
        output = {value: count for value, count in counter.most_common()}
        return SequenceCollection.from_unpacked(
            [PythonObjectPath(None, output)],
            order_paths=False,
            deduplicate_paths=False
        )