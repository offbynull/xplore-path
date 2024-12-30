from collections import Counter
from typing import Any

from xplore_path.invocable.invocable import Invocable
from xplore_path.path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


class WhitespaceStripInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        if type(result) != list:
            result = [result]
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        return [v.strip() if type(v) == str else v for v in values]