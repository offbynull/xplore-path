from __future__ import annotations

from xplore_path.entity import Entity
from xplore_path.core_type_utils import CoreTypeAlias
from xplore_path.fallback_mode import FallbackMode


class DefaultFallbackMode(FallbackMode):
    def __init__(self, default: Entity | CoreTypeAlias):
        if isinstance(default, Entity):
            self.default = default
        else:
            self.default = Entity(default)

    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        if x is None:
            return (self.default, )
        return (x, )
