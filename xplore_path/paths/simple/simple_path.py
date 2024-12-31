from __future__ import annotations

from typing import Hashable, Any

from xplore_path.path.path import Path


class SimplePath(Path):
    def __init__(self, parent: Path | None, label: Hashable | None, value: Any):
        super().__init__(parent, label, value)
        self.children = []

    def add_child(self, child_p: Path):
        if child_p.parent() != self:
            raise ValueError('Child must have this path as its parent')
        self.children.append(child_p)

    def clear_children(self):
        self.children = []

    def all_children(self) -> list[Path]:
        return self.children
