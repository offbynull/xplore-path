from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.sequence import FullSequence, SingleOrSequenceWrapSequence


class WhitespaceStripInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        result = SingleOrSequenceWrapSequence(result)
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        return FullSequence([v.strip() if type(v) == str else v for v in values])