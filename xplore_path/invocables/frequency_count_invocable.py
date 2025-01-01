from collections import Counter
from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class FrequencyCountInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        if type(result) != list:
            result = [result]
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        counter = Counter(values)
        return [PythonObjectPath(None, value, count) for value, count in counter.items()]