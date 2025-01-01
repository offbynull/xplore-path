from typing import Any

from xplore_path.invocable import Invocable


class CountInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        if type(result) != list:
            result = [result]
        return len(result)