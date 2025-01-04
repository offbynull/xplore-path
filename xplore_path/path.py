from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Hashable


class Path(ABC):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: Any
    ):
        self._parent = parent
        self._label = label
        self._value = value
        self._position_in_parent = position_in_parent

    @abstractmethod
    def all_children(self) -> list[Path]:
        ...

    def all_descendants(self, max_level: int = 100000) -> list[Path]:
        ret = []
        if max_level > 0:
            for pe in self.all_children():
                ret += [pe]
                ret += [p for p in pe.all_descendants(max_level - 1)]
        return ret

    def following(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[self_idx_in_siblings+1:]
        ret = []
        for p in siblings:
            ret += [p]
            ret += p.all_descendants()
        ret += parent_p.following()
        return ret

    def following_sibling(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[self_idx_in_siblings+1:]
        return siblings

    def parent(self) -> Path | None:
        return self._parent

    def position(self) -> int:
        if self._position_in_parent is None:
            raise ValueError('No parent')
        return self._position_in_parent

    def full_position(self) -> list[int]:
        p_list = []
        p = self
        while p is not None:
            p_list.append(p)
            p = p.parent()
        return [p.position() for p in reversed(p_list[:-1])]

    def all_ancestors(self) -> list[Path]:
        ret = []
        parent_p = self.parent()
        while parent_p is not None:
            ret.append(parent_p)
            parent_p = parent_p.parent()
        return ret

    def preceding(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[:self_idx_in_siblings]
        ret = parent_p.preceding() + [parent_p]
        for p in siblings:
            ret += [p]
            ret += p.all_descendants()
        return ret

    def preceding_sibling(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[:self_idx_in_siblings]
        return siblings

    def value(self) -> Any:
        return self._value

    def label(self) -> Hashable:
        return self._label

    def full_label(self) -> list[Any]:
        p_list = []
        p = self
        while p is not None:
            p_list.append(p)
            p = p.parent()
        return [p.label() for p in reversed(p_list)]

    def __str__(self):
        return f'{self.full_label()}: {self.value()}'
