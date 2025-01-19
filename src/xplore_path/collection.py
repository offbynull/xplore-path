"""
Entity collection.
"""

from __future__ import annotations

import itertools
from abc import ABC, abstractmethod
from typing import Callable, Literal, Iterator, Hashable

from xplore_path.entity import Entity
from xplore_path.core_types import CoreTypeAlias
from xplore_path.fallback_mode import FallbackMode
from xplore_path.node import Node


class Collection(ABC):
    """
    Collection of ``Entity``\s.
    """
    @abstractmethod
    def transform(
            self,
            transformer: Callable[[int, Entity], Entity | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        """
        Transform ``Entity``\s within this ``Collection``.

        :param transformer: ``Callable`` that transforms ``Entity``\s. The ``Callable`` takes 2 arguments: An index
            within this ``Collection`` and the ``Entity`` at that index. Each invocation of the ``Callable`` transforms
            the input ``Entity`` into a new output ``Entity``, or ``None`` if there was a problem while transforming.
        :param fallback_mode: Action to take when transformation fails (when an invocation of ``transformer``
            returns ``None``).
        :return: ``self`` transformed.
        """
        ...

    def transform_unpacked(
            self,
            transformer: Callable[[int, CoreTypeAlias], CoreTypeAlias | None],
            fallback_mode: FallbackMode
    ) -> Collection:
        """
        Equivalent to ``transform()``, but directly operates on the ``Entity`` values rather than the ``Entity``\s
        themselves.

        :param transformer: ``Callable`` that transforms ``Entity`` values. The ``Callable`` takes 2 arguments: An index
            within this ``Collection`` and the ``Entity`` value at that index. Each invocation of the ``Callable``
            transforms the input value into a new output value, or ``None`` if there was a problem while transforming.
        :param fallback_mode: Action to take when transformation fails (when an invocation of ``transformer`` returns
            ``None``).
        :return: ``self`` transformed.
        """
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
        """
        Filter ``Entity``\s within this ``Collection``.

        :param predicate: ``Callable`` that defines if an ``Entity`` should stay or be removed. The ``Callable`` takes 2
            arguments: An index within this ``Collection`` and the ``Entity`` at that index. Each invocation of the
            ``Callable`` returns a ``bool``, where ``True`` means keep and ``False`` means remove.
        :return: ``self`` filtered.
        """
        ...

    def filter_unpacked(
            self,
            predicate: Callable[[int, CoreTypeAlias], bool],
    ) -> Collection:
        """
        Equivalent to ``filter()``, but directly operates on the ``Entity`` values rather than the ``Entity``\s
        themselves.

        :param predicate: ``Callable`` that defines if an ``Entity`` should stay or be removed. The ``Callable`` takes 2
            arguments: An index within this ``Collection`` and the ``Entity`` value at that index. Each invocation of
            the ``Callable`` returns a ``bool``, where ``True`` means keep and ``False`` means remove.
        :return: ``self`` filtered.
        """
        return self.filter(lambda i, e: predicate(i, e.value))

    def to_set(self) -> dict[tuple[Literal['NODE'], tuple[int, ...]] | tuple[Literal['RAW'], Hashable], Entity]:
        """
        Transform this ``Collection`` to a dictionary for the purpose of set operations (e.g. union, intersect, etc..).
        Each dictionary entry is an ``Entity`` within this ``Collection``, where the dictionary key is a hashable value
        derived from the ``Entity`` and the dictionary value is the ``Entity`` itself. Specifically, each dictionary key
        is a 2-tuple, where ...

         * if the ``Entity``'s value is a ``Node``, item 1 is the string ``'NODE'`` and item 2 is
           ``entity.value.full_position()``.
         * if the ``Entity``'s value is not a ``Node``, item 1 is the string ``'RAW'`` and item 2 ``entity.value``
           (provided that ``entity.value`` is hashable -- if it isn't, the entry is silently discarded).

        :return: ``self`` as a dictionary.
        """
        ret = {}
        for v in self.unpack:
            if isinstance(v, Node):
                k = 'NODE', tuple(v.full_position())  # Don't use full_label() because labels aren't unique
            else:
                if not isinstance(v, Hashable):  # Discard any value that isn't hashable (matchers, invocables, etc..)
                    continue
                k = 'RAW', v
            ret[k] = Entity(v)
        return ret  # noqa

    @property
    def unpack(self) -> Iterator[CoreTypeAlias]:
        """
        Equivalent to ``(e.value for e in self)``.

        :return: Iterator that walks over this ``Collection``'s ``Entity`` values (as opposed to walking over the
            ``Entity``\s themselves).
        """
        return (e.value for e in self)

    @abstractmethod
    def __iter__(self):
        """
        Iterate over the ``Entity``\s contained within this ``Collection``.

        :return: Iterator that walks over this ``Collection``'s ``Entity``.
        """
        ...

    def __bool__(self):
        """
        Return ``True`` if this ``Collection`` is empty, ``False`` otherwise.

        :return: ``True`` if this ``Collection`` is empty, ``False`` otherwise.
        """
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


