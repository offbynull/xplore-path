from typing import Any

from xplore_path.coercer_fallback import CoercerFallback


class DiscardCoercerFallback(CoercerFallback):
    def coerce(self, value: list[Any]) -> list[Any]:
        return [v for v in value if v is not None]