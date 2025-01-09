import re
from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.sequence import SingleOrSequenceWrapSequence, FullSequence


class WhitespaceRemoveInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, = args
        result = SingleOrSequenceWrapSequence(result)
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        return FullSequence([re.sub(r'\s+', '', v) if type(v) == str else v for v in values])