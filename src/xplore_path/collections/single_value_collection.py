from __future__ import annotations

import itertools
from typing import Callable

from xplore_path.collection import Collection
from xplore_path.fallback_mode import FallbackMode
from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.entity import Entity, BasicType


class SingleValueCollection(Collection):
    def __init__(
            self,
            value: Entity | BasicType
    ):
        if not isinstance(value, Entity):
            value = Entity(value)
        self._value = value

    def transform(
            self,
            transformer: Callable[[int, Entity], Entity | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        ret = transformer(0, self._value)
        ret = fallback_mode.evaluate(ret)
        if not ret:
            return SequenceCollection.empty()
        return SingleValueCollection(ret[0])

    def filter(
            self,
            predicate: Callable[[int, Entity], bool]
    ) -> Collection:
        if predicate(0, self._value):
            return self
        return SequenceCollection.empty()

    @property
    def single(self):
        return self._value

    def __iter__(self):
        return itertools.repeat(self._value, 1)

    def __bool__(self):
        return True

    def __eq__(self, other):
        if not isinstance(other, Collection):
            other = SingleValueCollection(other)
        return super().__eq__(other)

    def __str__(self):
        return str(self._value)