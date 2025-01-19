"""
Entity collection, backed by a listed.
"""
from __future__ import annotations

import itertools
from typing import Iterable, Callable, Iterator

from xplore_path.collection import Collection
from xplore_path.fallback_mode import FallbackMode
from xplore_path.entity import Entity
from xplore_path.core_types import CoreTypeAlias
from xplore_path.node import Node


class SequenceCollection(Collection):
    """
    ``Collection`` backed by a list (sequence).
    """
    def __init__(
            self,
            entities: Iterator[Entity],
            order_nodes: bool,
            deduplicate_nodes: bool
    ):
        """
        Construct a ``SequenceCollection`` object.

        :param entities: ``Entity``\s to insert into this ``Collection``. For ``Entity``\s that wrap a ``Node``,
            those ``Node``\s must all be from the same hierarchy (must all have the same root), otherwise the behavior of
            this class is undefined.
        :param order_nodes: If ``True``, ``entities`` is re-ordered such that ...

             * ``Entity``\s wrapping ``Node`` go first, ordered on ``entity.value.full_position()`` (document order).
             * ``Entity``\s wrapping non-``Node`` go last, maintaining the same order as within ``entities``.

            Otherwise, ``entities`` maintains the order it has.
        :param deduplicate_nodes: If ``True``, ``entities`` wrapping ``Node``\s are deduplicated such that no ``Node``
            appears more than once. Note that duplicate ``Node``\s are determined by checking for conflicting
            ``entity.value.full_position()``, which only works if all ``Node``\s are within the same hierarchy (must all
            have the same root).

            Otherwise, ``entities`` wrapping ``Node``\s are not deduplicated.
        """
        super().__init__()
        if order_nodes:
            paths = []
            non_paths = []
            for e in entities:
                if isinstance(e.value, Node):
                    paths.append(e.value)
                else:
                    non_paths.append(e.value)
            # NOTE: entities is no longer usable at this point
            paths.sort(key=lambda p: p.full_position())
            if deduplicate_nodes and len(paths) > 0:
                write_ptr = 0
                for read_ptr in range(1, len(paths)):
                    if paths[read_ptr].full_position() == paths[write_ptr].full_position():
                        continue
                    write_ptr += 1
                    paths[write_ptr] = paths[read_ptr]
                paths = paths[:write_ptr+1]
            new_values = paths + non_paths
        elif deduplicate_nodes:
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
            order_nodes: bool = True,
            deduplicate_nodes: bool = True
    ) -> SequenceCollection:
        """
        Create ``SequenceCollection`` by wrapping each element of ``values`` as an ``Entity`` and passing it to the
        constructor.

        :param values: Values to insert into created ``SequenceCollection``. These values are transformed such that each
            is wrapped within an ``Entity`` before they're all passed in to the constructor's ``entities`` parameter.
            Note that, unlike the constructor's ``entities`` parameter, this may be an ``Iterable``.
        :param order_nodes: See description of similarly named parameter in constructor.
        :param deduplicate_nodes: See description of similarly named parameter in constructor.
        :return: Newly created ``SequenceCollection`` object.
        """
        if isinstance(values, Iterator):
            values = iter(values)
        return SequenceCollection((Entity(v) for v in values), order_nodes, deduplicate_nodes)

    @staticmethod
    def from_entities(
            entities: Iterator[Entity] | Iterable[Entity],
            order_nodes: bool = True,
            deduplicate_nodes: bool = True
    ) -> SequenceCollection:
        """
        Create ``SequenceCollection``.

        :param entities: See description of similarly named parameter in constructor. Note that, unlike the
            constructor's ``entities`` parameter, this may be an ``Iterable``.
        :param order_nodes: See description of similarly named parameter in constructor.
        :param deduplicate_nodes: See description of similarly named parameter in constructor.
        :return: Newly created ``SequenceCollection`` object.
        """
        if isinstance(entities, Iterator):
            entities = iter(entities)
        return SequenceCollection(entities, order_nodes, deduplicate_nodes)

    @staticmethod
    def empty() -> SequenceCollection:
        """
        Create empty ``SequenceCollection``.

        :return: Newly created ``SequenceCollection`` object, which is empty.
        """
        return SequenceCollection(iter([]), False, False)
