from typing import Any

from xplore_path.coercer_fallback import CoercerFallback


class DefaultCoercerFallback(CoercerFallback):
    def __init__(self, default: Any):
        self.default = default

    def coerce(self, value: list[Any]) -> list[Any]:
        return [v if v is not None else self.default for v in value]