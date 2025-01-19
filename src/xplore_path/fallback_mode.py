"""``Entity`` error fallback mode."""
from __future__ import annotations

from abc import ABC, abstractmethod

from xplore_path.entity import Entity


class FallbackMode(ABC):
    """
    ``Entity`` error fallback mode.
    """
    @abstractmethod
    def evaluate(self, x: Entity | None) -> tuple[Entity] | ():
        """
        Evaluate an ``Entity`` for errors. This handler may choose to either ...

         * discard the entity (return a 0-tuple).
         * keep/replace the entity (return a 1-tuple).
         * error out (raise ``ValueError``).

        Errors come in two forms / cases:

        1. The ``Entity`` being evaluated is set to ``None``, which means that some upstream processing failed to
           generate the ``Entity``. This case is always evaluated as an error and must be handled.
        2. The ``Entity`` being evaluated is not ``None`` but still is deemed as being invalid state by this function.
           For example, the function may reject any ``Entity`` containing a negative integer.

        :param x: Entity being evaluated for an error, which may be ``None`` if there was an error generating the Entity
            upstream.
        :return: Either a 0-tuple or a 1-tuple, where the 0-tuple indicates that ``x`` should be discarded and a 1-tuple
            indicates that ``x`` should be replaced with the ``Entity`` within that 1-tuple (which may or may not be the
            same object as ``x``).
        :raises ValueError: If this function determines that the best way to handle ``x`` being erroneous is to raise an
            error.
        """
        ...
