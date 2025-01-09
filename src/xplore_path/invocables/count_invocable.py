from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.sequence import SingleOrSequenceWrapSequence


class CountInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        result = SingleOrSequenceWrapSequence(result)
        return sum(1 for _ in result)