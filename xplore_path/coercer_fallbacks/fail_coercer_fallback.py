from typing import Any

from xplore_path.coercer_fallback import CoercerFallback


class FailCoerecerFallback(CoercerFallback):
    def coerce(self, value: list[Any]) -> list[Any]:
        if any(v for v in value if v is None):
            raise ValueError('Failed to coerce')
        return value