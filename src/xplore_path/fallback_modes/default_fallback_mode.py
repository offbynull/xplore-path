"""
``FallbackMode`` that returns a default value on error.
"""
from __future__ import annotations

from xplore_path.entity import Entity
from xplore_path.core_types import CoreTypeAlias
from xplore_path.fallback_mode import FallbackMode


class DefaultFallbackMode(FallbackMode):
    """
    ``FallbackMode`` that returns a default value on error.
    """
    def __init__(self, default: Entity | CoreTypeAlias):
        """
        Construct a ``DefaultFallbackMode`` object.

        :param default: Default ``Entity`` to replace errors with. If ``default``'s type isn't ``Entity``, it's
            internally wrapped as an ``Entity``.
        """
        if isinstance(default, Entity):
            self.default = default
        else:
            self.default = Entity(default)

    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        if x is None:
            return (self.default, )
        return (x, )
