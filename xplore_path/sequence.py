from __future__ import annotations

import itertools
from abc import ABC, abstractmethod
from typing import Any, Iterable, Iterator, Callable

from xplore_path.path import Path


class Sequence(ABC):
    def __init__(self):
        ...

    @abstractmethod
    def _walk_entities(self) -> Iterator[Path | Any]:
        ...

    def to_values(self) -> Iterator[Path | Any]:
        return ((v.value() if isinstance(v, Path) else v) for v in self._walk_entities())

    def __iter__(self):
        return self._walk_entities()

    def __bool__(self):
        try:
            next(iter(self))
            return True
        except StopIteration:
            return False

    def __eq__(self, other):
        if not (isinstance(other, Sequence) or isinstance(other, list)):
            return False
        sentinel = object()
        for val1, val2 in itertools.zip_longest(self, other, fillvalue=sentinel):
            if val1 is sentinel or val2 is sentinel or val1 != val2:
                return False
        return True


class FallbackMode(ABC):
    @abstractmethod
    def evaluate(self, x: Any) -> tuple[Any]:
        ...

class DiscardFallbackMode(FallbackMode):
    def evaluate(self, x: Any) -> tuple[Any]:
        if x is None:
            return tuple()
        return (x, )

class ErrorFallbackMode(FallbackMode):
    def evaluate(self, x: Any) -> tuple[Any]:
        if x is None:
            raise ValueError('None not allowed')
        return (x, )

class DefaultFallbackMode(FallbackMode):
    def __init__(self, default: Any):
        self.default = default

    def evaluate(self, x: Any) -> tuple[Any]:
        if x is None:
            return (self.default, )
        return (x, )

class DoNothingFallbackMode(FallbackMode):
    def evaluate(self, x: Any) -> tuple[Any]:
        return (x, )


class TransformSequence(Sequence):
    def __init__(
            self,
            sequence: Sequence,
            transformer: Callable[[int, Any], Any],
            fallback_mode: FallbackMode | Any
    ):
        super().__init__()
        self._sequence = sequence
        self._transformer = transformer
        self._fallback_mode = fallback_mode

    def _walk_entities(self) -> Iterator[Path | Any]:
        ret = (self._transformer(i, e) for i, e in enumerate(self._sequence))
        ret = itertools.chain(*(self._fallback_mode.evaluate(e) for e in ret))
        return ret


class FilterSequence(Sequence):
    def __init__(
            self,
            sequence: Sequence,
            predicate: Callable[[int, Any], Any],
    ):
        super().__init__()
        self._sequence = sequence
        self._predicate = predicate

    def _walk_entities(self) -> Iterator[Path | Any]:
        ret = (e for i, e in enumerate(self._sequence) if self._predicate(i, e))
        return ret


class EmptySequence(Sequence):
    def __init__(self):
        super().__init__()

    def _walk_entities(self) -> Iterator[Path | Any]:
        return itertools.chain()


class SingleWrapSequence(Sequence):
    def __init__(self, backing: Any):
        super().__init__()
        self._backing = backing

    def _walk_entities(self) -> Iterator[Path | Any]:
        return itertools.repeat(self._backing, times=1)


class SingleOrSequenceWrapSequence(Sequence):
    def __init__(self, backing: Sequence | Any):
        super().__init__()
        self._backing = backing

    def _walk_entities(self) -> Iterator[Path | Any]:
        if isinstance(self._backing, Sequence):
            return self._backing._walk_entities()
        else:
            return itertools.repeat(self._backing, times=1)


class FullSequence(Sequence):
    def __init__(
            self,
            entities: Iterable[Path | Any],
            order_paths: bool = True,
            deduplicate_paths: bool = True
    ):
        super().__init__()
        if order_paths:
            paths = []
            non_paths = []
            for e in entities:
                if isinstance(e, Path):
                    paths.append(e)
                else:
                    non_paths.append(e)
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
            new_entities = paths + non_paths
        elif deduplicate_paths:
            paths = []
            non_paths = []
            for e in entities:
                if isinstance(e, Path):
                    paths.append(e)
                else:
                    non_paths.append(e)
            # NOTE: entities is no longer usable at this point
            paths = list({v.full_position(): v for v in paths if isinstance(v, Path)}.values())
            new_entities = paths + non_paths
        else:
            new_entities = list(entities)
        self._values = new_entities

    def _walk_entities(self) -> Iterator[Path | Any]:
        return iter(self._values)

    def __iter__(self):
        return iter(self._values)
