from typing import Any

from xplore_path.invocable.invocable import Invocable
from xplore_path.path.path import Path


class DistinctInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        if type(result) != list:
            result = [result]
        return list({v.value() if isinstance(v, Path) else v for v in result})