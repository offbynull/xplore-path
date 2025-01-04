from collections import Counter
from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath
from xplore_path.sequence import SingleOrSequenceWrapSequence, FullSequence


class FrequencyCountInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        result = SingleOrSequenceWrapSequence(result)
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        counter = Counter(values)
        return FullSequence(
            (PythonObjectPath(None, 0, value, count) for value, count in counter.items()),
            order_paths=False,
            deduplicate_paths=False
        )