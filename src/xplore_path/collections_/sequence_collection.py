from __future__ import annotations

import itertools
from typing import Iterable, Callable, Iterator

from xplore_path.collection import Collection
from xplore_path.fallback_mode import FallbackMode
from xplore_path.entity import Entity
from xplore_path.core_type_utils import CoreTypeAlias
from xplore_path.node import Node


class SequenceCollection(Collection):
    def __init__(
            self,
            entities: Iterator[Entity],
            order_paths: bool,
            deduplicate_paths: bool
    ):
        super().__init__()
        if order_paths:
            paths = []
            non_paths = []
            for e in entities:
                if isinstance(e.value, Node):
                    paths.append(e.value)
                else:
                    non_paths.append(e.value)
            # NOTE: entities is no longer usable at this point
            paths.sort(key=lambda p: p.full_position())
            if deduplicate_paths and len(paths) > 0:
                write_ptr = 0
                for read_ptr in range(1, len(paths)):
                    if paths[read_ptr].full_position() == paths[write_ptr].full_position():
                        continue
                    write_ptr += 1
                    paths[write_ptr] = paths[read_ptr]
                paths = paths[:write_ptr+1]
            new_values = paths + non_paths
        elif deduplicate_paths:
            paths = []
            non_paths = []
            for e in entities:
                if isinstance(e.value, Node):
                    paths.append(e.value)
                else:
                    non_paths.append(e.value)
            # NOTE: entities is no longer usable at this point
            paths = list({tuple(v.full_position()): v for v in paths if isinstance(v, Node)}.values())
            new_values = paths + non_paths
        else:
            new_values = [e.value for e in entities]
        self._values = [Entity(v) for v in new_values]

    def transform(
            self,
            transformer: Callable[[int, Entity], Entity | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        ret = (transformer(i, e) for i, e in enumerate(self))
        ret = itertools.chain(*(fallback_mode.evaluate(e) for e in ret))
        return SequenceCollection(ret, False, False)

    def filter(
            self,
            predicate: Callable[[int, Entity], bool]
    ) -> Collection:
        ret = (e for i, e in enumerate(self) if predicate(i, e))
        return SequenceCollection(ret, False, False)

    def __iter__(self):
        return iter(self._values)

    def __bool__(self):
        return len(self._values) > 0

    def __eq__(self, other):
        if isinstance(other, Iterable) and not isinstance(other, Collection):
            other = SequenceCollection.from_unpacked(other, False, False)
        return super().__eq__(other)

    def __str__(self):
        return '\n'.join(f'{v.value}' for v in self)

    @staticmethod
    def from_unpacked(
            values: Iterator[CoreTypeAlias] | Iterable[CoreTypeAlias],
            order_paths: bool = True,
            deduplicate_paths: bool = True
    ) -> SequenceCollection:
        if isinstance(values, Iterator):
            values = iter(values)
        return SequenceCollection((Entity(v) for v in values), order_paths, deduplicate_paths)

    @staticmethod
    def from_entities(
            entities: Iterator[Entity] | Iterable[Entity],
            order_paths: bool = True,
            deduplicate_paths: bool = True
    ) -> SequenceCollection:
        if isinstance(entities, Iterator):
            entities = iter(entities)
        return SequenceCollection(entities, order_paths, deduplicate_paths)

    @staticmethod
    def empty() -> SequenceCollection:
        return SequenceCollection(iter([]), False, False)
