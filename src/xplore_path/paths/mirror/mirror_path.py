from __future__ import annotations

from typing import Any

from xplore_path.path import Path, ParentBlock


class MirrorPath(Path):
    def __init__(
            self,
            backing_path: Path,
            new_parent: ParentBlock | None,  # None for root
    ):
        super().__init__(
            new_parent,
            backing_path.value()
        )
        self.backing_path = backing_path

    def all_children(self) -> list[Path]:
        ret = []
        for child_p in self.backing_path.all_children():
            child_p = MirrorPath(child_p, ParentBlock(self, child_p.position(), child_p.label()))
            ret.append(child_p)
        return ret
