from __future__ import annotations

from typing import Any

from xplore_path.entity import Entity
from xplore_path.fallback_mode import FallbackMode


class DefaultFallbackMode(FallbackMode):
    def __init__(self, default: Entity):
        self.default = default

    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        if x is None:
            return (self.default, )
        return (x, )
