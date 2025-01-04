import re
from typing import Any

from xplore_path.invocable import Invocable
from xplore_path.path import Path
from xplore_path.sequence import SingleOrSequenceWrapSequence, FullSequence


class RegexExtractInvocable(Invocable):
    def invoke(self, args: list[Any]) -> Any:
        result, pattern = args
        result = SingleOrSequenceWrapSequence(result)
        values = [v.value() if isinstance(v, Path) else v for v in result]
        values = [v for v in values if type(v) in {str, int, float, bool}]
        values = [str(v) for v in values]
        values = [re.search(pattern, v) for v in values]
        values = [v.group(0) for v in values if v]
        return FullSequence(values)