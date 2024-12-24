from __future__ import annotations

import types
from dataclasses import dataclass
from typing import Any


@dataclass
class PathElement:
    label: Any
    value: Any


class Path:
    def __init__(self, elements: list[PathElement]):
        if len(elements) == 0:
            raise ValueError('Must have at least 1 element')
        self._elements = elements[:]

    def all_children(self) -> list[Path]:
        parent = self._elements[-1].value
        ret = []
        if isinstance(parent, dict):
            for k in parent.keys():
                ret += [self + PathElement(k, parent[k])]
        elif isinstance(parent, set):
            for k in parent:
                return [self + PathElement(k, k in parent)]
        elif isinstance(parent, (list, tuple)):
            for k in range(len(parent)):
                ret += [self + PathElement(k, parent[k])]
        for k in dir(parent):
            if k.startswith('_'):
                continue
            v = getattr(parent, k)
            if type(v) in {str, int, float, bool, types.BuiltinFunctionType, types.BuiltinMethodType}:
                continue
            ret += [self + PathElement(k, v)]
        return ret

    def all_descendants(self, max_level: int = 100000) -> list[Path]:
        ret = self.all_children()
        if max_level > 0:
            for pe in self.all_children():
                ret += [p for p in pe.all_descendants(max_level - 1)]
        return ret

    def following(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.last().label == self.last().label)
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
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.last().label == self.last().label)
        siblings = siblings[self_idx_in_siblings+1:]
        return siblings

    def parent(self) -> Path | None:
        if len(self._elements) > 1:
            return Path(self._elements[:-1])
        return None

    def position_in_parent(self) -> int:
        p = self.parent()
        if p is None:
            raise ValueError('No parent')
        return [c.last().label for c in p.all_children()].index(self.last().label)

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
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.last().label == self.last().label)
        siblings = siblings[:self_idx_in_siblings]
        ret = []
        for p in siblings:
            ret += [p]
            ret += p.all_descendants()
        ret += parent_p.preceding()
        return ret[::-1]

    def preceding_sibling(self) -> list[Path]:
        parent_p = self.parent()
        if parent_p is None:
            return []
        siblings = parent_p.all_children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.last().label == self.last().label)
        siblings = siblings[:self_idx_in_siblings]
        return siblings[::-1]

    def first(self) -> PathElement:
        return self._elements[0]

    def last(self) -> PathElement:
        return self._elements[-1]

    def label(self) -> list[Any]:
        p_list = []
        p = self
        while p is not None:
            p_list.append(p)
            p = p.parent()
        return [p.last().label for p in reversed(p_list)]

    def __add__(self, other: PathElement | list[PathElement] | Path) -> Path:
        if isinstance(other, Path):
            return Path(self._elements + other._elements)
        if isinstance(other, list):
            return Path(self._elements + [other])
        if isinstance(other, PathElement):
            return Path(self._elements + [other])
        raise ValueError('Unexpected input')

    def __contains__(self, item):
        return item in self._elements

    def __iter__(self):
        return iter(self._elements)

    def __getitem__(self, index):
        return self._elements[index]


if __name__ == '__main__':
    x = { 1: 'z', 'a': { 'b': { 'c': 1, 'd': 2 } } }
    path = Path([PathElement(None, x)])
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')