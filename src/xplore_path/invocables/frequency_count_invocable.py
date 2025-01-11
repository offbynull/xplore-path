from collections import Counter

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.collection import Collection
from xplore_path.collections.sequence_collection import SequenceCollection


class FrequencyCountInvocable(Invocable):
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        values = [v.value() if isinstance(v, Path) else v for v in result.unpack]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        counter = Counter(values)
        output = {value: count for value, count in counter.most_common()}
        return SequenceCollection.from_unpacked(
            [PythonObjectPath(None, None, None, output)],
            order_paths=False,
            deduplicate_paths=False
        )