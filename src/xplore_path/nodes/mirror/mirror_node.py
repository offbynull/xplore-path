from __future__ import annotations

from typing import Any

from xplore_path.node import Node, ParentBlock


class MirrorNode(Node):
    def __init__(
            self,
            backing_path: Node,
            new_parent: ParentBlock | None,  # None for root
    ):
        super().__init__(
            new_parent,
            backing_path.value()
        )
        self.backing_path = backing_path

    def children(self) -> list[Node]:
        ret = []
        for child_p in self.backing_path.children():
            child_p = MirrorNode(child_p, ParentBlock(self, child_p.position(), child_p.label()))
            ret.append(child_p)
        return ret
