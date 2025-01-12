from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from xplore_path.null import Null
if TYPE_CHECKING:
    from xplore_path.core_type_utils import CoreTypeAlias


@dataclass
class ParentBlock:
    parent_path: Path
    child_position: int
    child_label: str | int | float | bool


class Path(ABC):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            value: CoreTypeAlias | None  # None means non-existent value, which is different from Null
    ):
        self._parent = None if parent is None else parent.parent_path
        self._label = None if parent is None else parent.child_label
        self._position = None if parent is None else parent.child_position
        self._value = value

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
        if type(parent_p) == Null:
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
        if type(parent_p) == Null:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[self_idx_in_siblings+1:]
        return siblings

    def parent(self) -> Path | Null:
        if self._parent is None:
            return Null()
        return self._parent

    def position(self) -> int | Null:
        if self._position is None:
            return Null()
        return self._position

    def full_position(self) -> list[int]:
        p_list = []
        p = self
        while type(p) != Null:
            p_list.append(p)
            p = p.parent()
        return [p.position() for p in reversed(p_list[:-1])]

    def all_ancestors(self) -> list[Path]:
        ret = []
        parent_p = self.parent()
        while type(parent_p) != Null:
            ret.append(parent_p)
            parent_p = parent_p.parent()
        return ret

    def preceding(self) -> list[Path]:
        parent_p = self.parent()
        if type(parent_p) == Null:
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
        if type(parent_p) == Null:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[:self_idx_in_siblings]
        return siblings

    def value(self) -> CoreTypeAlias | None:  # why None? In some cases, it'll have children but no value (no value = None, which is different from Null)
        return self._value

    def label(self) -> str | int | float | bool | Null:
        if self._label is None:
            return Null()
        return self._label

    def full_label(self) -> list[str | int | float | bool]:
        p_list = []
        p = self
        while type(p) != Null:
            p_list.append(p)
            p = p.parent()
        return [p.label() for p in reversed(p_list[:-1])]

    def to_dict(self) -> dict[str | int | float | bool | Null, tuple[CoreTypeAlias | None, dict]]:
        ret = {}
        for pe in self.all_children():
            ret[pe.label()] = (pe.value(), pe.to_dict())
        return ret

    def __str__(self):
        return f'Path({self.full_label()}, {self.value()})'
