from __future__ import annotations

from typing import Any

from xplore_path.entity import Entity
from xplore_path.fallback_mode import FallbackMode


class DiscardFallbackMode(FallbackMode):
    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        if x is None:
            return tuple()
        return (x, )
