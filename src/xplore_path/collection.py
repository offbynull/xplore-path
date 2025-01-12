from __future__ import annotations

import itertools
from abc import ABC, abstractmethod
from typing import Callable, Literal, Iterator

from xplore_path.entity import Entity
from xplore_path.core_type_utils import CoreTypeAlias
from xplore_path.fallback_mode import FallbackMode
from xplore_path.path import Path


class Collection(ABC):
    @abstractmethod
    def transform(
            self,
            transformer: Callable[[int, Entity], Entity | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        ...

    def transform_unpacked(
            self,
            transformer: Callable[[int, CoreTypeAlias], CoreTypeAlias | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        def _(idx: int, e: Entity) -> Entity | None:
            ret = transformer(idx, e.value)
            if ret is None:
                return None
            else:
                return Entity(ret)

        return self.transform(lambda i, e: _(i, e), fallback_mode)

    @abstractmethod
    def filter(
            self,
            predicate: Callable[[int, Entity], bool],
    ) -> Collection:
        ...

    def filter_unpacked(
            self,
            predicate: Callable[[int, CoreTypeAlias], bool],
    ) -> Collection:
        return self.filter(lambda i, e: predicate(i, e.value))

    def to_set(self) -> dict[tuple[Literal['PATH', 'RAW'], tuple[str | int | float | bool | None, ...]], Entity]:
        ret = {}
        for v in self.unpack:
            if isinstance(v, Path):
                k = 'PATH', tuple(v.full_label())
            else:
                if not isinstance(v, (str, int, float, bool, None)):  # discard matchers, invocables, etc..
                    continue
                k = 'RAW', v
            try:
                ret[k] = Entity(v)
            except TypeError:
                ...  # type is unhashable? silently discard it and move on
        return ret  # noqa

    @property
    def unpack(self) -> Iterator[CoreTypeAlias]:
        return (e.value for e in self)

    @abstractmethod
    def __iter__(self):
        ...

    def __bool__(self):
        try:
            next(iter(self))
            return True
        except StopIteration:
            return False

    def __eq__(self, other):
        if not isinstance(other, Collection):
            return False
        sentinel = object()
        for val1, val2 in itertools.zip_longest(self, other, fillvalue=sentinel):
            if val1 is sentinel or val2 is sentinel or val1 != val2:
                return False
        return True

    def __str__(self):
        return '\n'.join(f'{v}' for v in self)


