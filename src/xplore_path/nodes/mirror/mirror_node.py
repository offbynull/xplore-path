from __future__ import annotations

from typing import Any

from xplore_path.node import Node, ParentBlock


class MirrorNode(Node):
    """
    ``Node`` that wraps another node, presenting it as if it has a different parent.
    """
    def __init__(
            self,
            backing_node: Node,
            new_parent: ParentBlock | None
    ):
        """
        Construct a ``MirrorNode`` object.

        :param backing_node: ``Node`` backing this ``Node``.
        :param new_parent: Attributes defining this ``Node`` in relation to its parent, or ``None`` if this node has no
            parent (it represents root). ``new_parent`` overrides the parent of ``backing_node``.
        """
        super().__init__(
            new_parent,
            backing_node.value()
        )
        self._backing_path = backing_node

    def children(self) -> list[Node]:
        ret = []
        for child_p in self._backing_path.children():
            child_p = MirrorNode(child_p, ParentBlock(self, child_p.position(), child_p.label()))
            ret.append(child_p)
        return ret
