from __future__ import annotations

from typing import Any

from xplore_path.path import Path


class MirrorPath(Path):
    def __init__(
            self,
            backing_path: Path,
            new_parent: Path | None = None,
            new_position_in_parent: int | None = None,
            new_label: Any | None = None
    ):
        super().__init__(
            new_parent,
            new_position_in_parent,
            new_label if new_label is not None else backing_path.label(),
            backing_path.value()
        )
        self.backing_path = backing_path

    def all_children(self) -> list[Path]:
        ret = []
        for child_p in self.backing_path.all_children():
            child_p = MirrorPath(child_p, self, child_p.position())
            ret.append(child_p)
        return ret
