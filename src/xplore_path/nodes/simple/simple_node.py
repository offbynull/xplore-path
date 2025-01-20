from __future__ import annotations

from xplore_path.core_types import CoreTypeAlias
from xplore_path.node import Node, ParentBlock


class SimpleNode(Node):
    """
    ``Node`` whose children are manually added in (as opposed to being backed by some data structure). Prior to
    performing a query, all children must be added via ``add_child()`` and the object must be sealed via ``seal()``.
    It's illegal for this object ...

     * to be queried prior to invoking ``seal()``.
     * to have children added after invoking ``seal()``.
    """
    def __init__(
            self,
            parent: ParentBlock | None,
            value: CoreTypeAlias | None
    ):
        """
        Construct a ``SimpleNode`` object.

        :param parent: Attributes defining this node in relation to its parent, or ``None`` if this node has no parent
            (it represents root).
        :param value: Scalar value assigned to this node, or ``None`` if this node has no scalar value (which is
            different from a scalar value of ``Null``).
        """
        super().__init__(parent, value)
        self._children = []
        self._sealed = False

    def add_child(self, child: Node) -> None:
        """
        Add a child.
        :param child: Child node.
        :raises ValueError: If ``seal()`` has already been invoked.
        :raises ValueError: If ``child`` does not have ``self`` as its parent.
        :raises ValueError: If ``child`` does not have the expected parent position (e.g. if 3 children have already
            been added, ``child`` would have to have position 3 because positions 0, 1, and 2 already exist).
        """
        if self._sealed:
            raise ValueError('Once sealed children can no longer be updated')
        if child.parent() != self:
            raise ValueError('Child must have this path as its parent')
        if child.position() != len(self._children):
            raise ValueError(f'Child must have position {len(self._children)}')
        self._children.append(child)

    def children(self) -> list[Node]:
        """
        List children.

        :return: Nodes that are children of this node, ordered ascending based on ``full_position()`` (document order).
        :raises ValueError: If ``seal()`` has not yet been invoked.
        """
        if not self._sealed:
            raise ValueError('Must seal to use')
        return self._children

    def seal(self) -> None:
        """
        Seal this object, such that the object can be queried and no further children can be manually added.

        Only the first invocation of this method has an effect. Subsequent invocations do nothing.
        """
        self._sealed = True
