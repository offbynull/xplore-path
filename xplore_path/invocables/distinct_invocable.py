from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.sequence import SingleOrSequenceWrapSequence, FullSequence


class DistinctInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        result = SingleOrSequenceWrapSequence(result)
        return FullSequence({v.value() if isinstance(v, Path) else v for v in result})