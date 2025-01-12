from __future__ import annotations

from xplore_path.core_type_utils import CoreTypeAlias
from xplore_path.path import Path


class SimplePath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: str | int | float | bool | None,  # None for root
            value: CoreTypeAlias | None  # None means non-existent value, which is different from Null
    ):
        super().__init__(parent, position_in_parent, label, value)
        self._children = []
        self._sealed = False

    def add_child(self, child_p: Path):
        if self._sealed:
            raise ValueError('Once sealed children can no longer be updated')
        if child_p.parent() != self:
            raise ValueError('Child must have this path as its parent')
        if child_p.position() != len(self._children):
            raise ValueError(f'Child must have position {len(self._children)}')
        self._children.append(child_p)

    def all_children(self) -> list[Path]:
        if not self._sealed:
            raise ValueError('Must seal to use')
        return self._children

    def seal(self) -> None:
        self._sealed = True
