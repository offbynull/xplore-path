from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TYPE_CHECKING

from xplore_path.null import Null
if TYPE_CHECKING:
    from xplore_path.core_types import CoreTypeAlias


@dataclass
class ParentBlock:
    """
    A node's attributes in relation to its parent.
    """
    parent: Node
    """Parent node."""
    child_position: int
    """Position of child within parent node."""
    child_label: str | int | float | bool
    """Label of child within parent node."""

    def __post_init__(self):
        if self.child_position < 0:
            raise ValueError('child_position must be > 0')


class Node(ABC):
    """
    A representation of a node within a hierarchy, starting at the root node of the hierarchy. Each node in the
    hierarchy ...

     * can have a scalar value: String, int, double, bool, null, ...
     * can have children.
     * has a parent, unless it's the root node.
     * has a position (relative to parent), unless it's the root node.
     * has a label (relative to parent), unless it's the root node.
    """
    def __init__(
            self,
            parent: ParentBlock | None,
            value: CoreTypeAlias | None
    ):
        """
        Construct a ``Node`` object.

        :param parent: Attributes defining this node in relation to its parent, or ``None`` if this node has no parent
            (it represents root).
        :param value: Scalar value assigned to this node, or ``None`` if this node has no scalar value (which is
            different from a scalar value of ``Null``).

            How is ``None`` different ``Null``? ``Null`` means that the node's scalar value is explicitly set to absent
            (e.g. a JSON field set to ``null``), while ``None`` means that the scalar value is missing (e.g. a JSON
            field set to a list - the field has children but having children means its impossible for it to have a
            scalar value). The distinction is important when it comes to formats like JSON, where a node must have
            either a scalar value (including ``null``) or have children, but not both. For example, the user may want to
            search through a set of JSON nodes for those explicitly set to ``null``, which are distinct from nodes that
            are missing scalar values due to having children.
        """
        # TODO: It may be better to remove the distinction between Null vs None and just use one of them for everything
        #       - then, add a metadata flag or attribute or something that represents how the value should be
        #       interpreted when querying / how it should be shown in the REPL?
        self._parent = None if parent is None else parent.parent
        self._label = None if parent is None else parent.child_label
        self._position = None if parent is None else parent.child_position
        self._value = value

    @abstractmethod
    def children(self) -> list[Node]:
        """
        List children.

        :return: Nodes that are children of this node, ordered ascending based on ``full_position()`` (document order).
        """
        ...

    def descendants(self, max_depth: int = 100000) -> list[Node]:
        """
        List descendants (children, children of children, children of children of children, ...).

        :param max_depth: Maximum descend depth.
        :return: Nodes that descend from this node, ordered ascending based on ``full_position()`` (document order).
        """
        ret = []
        if max_depth > 0:
            for pe in self.children():
                ret += [pe]
                ret += [p for p in pe.descendants(max_depth - 1)]
        return ret

    def following(self) -> list[Node]:
        """
        List nodes following this node in the overall hierarchy, as if invoking ``descendants()`` on the root node and
        filtering such that only nodes after this node are returned.

        :return: Nodes following this node in the overall hierarchy, ordered ascending based on ``full_position()``
            (document order).
        """
        parent_p = self.parent()
        if type(parent_p) == Null:
            return []
        siblings = parent_p.children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[self_idx_in_siblings+1:]
        ret = []
        for p in siblings:
            ret += [p]
            ret += p.descendants()
        ret += parent_p.following()
        return ret

    def following_sibling(self) -> list[Node]:
        """
        List sibling nodes following this node, as if invoking ``parent().children()`` and filtering such that only
        nodes after this node are returned.

        :return: Sibling nodes following this node in the overall hierarchy, ordered ascending based on
            ``full_position()`` (document order).
        """
        parent_p = self.parent()
        if type(parent_p) == Null:
            return []
        siblings = parent_p.children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[self_idx_in_siblings+1:]
        return siblings

    def parent(self) -> Node | Null:
        """
        Get parent.

        :return: Parent node, or ``Null`` if this node has no parent (node is root).
        """
        if self._parent is None:
            return Null()
        return self._parent

    def position(self) -> int | Null:
        """
        Get position of this node within its parent, as if invoking ``parent().children()`` and finding the index of
        this node in the results.

        :return: Position of this node within parent, or ``Null`` if this node has no parent (node is root).
        """
        if self._position is None:
            return Null()
        return self._position

    def full_position(self) -> list[int]:
        """
        Get positions of nodes descending to this node, as if invoking ``position()`` on each element of
        ``ancestors()[1:] + [self]``.

        :return: Position of ancestors and this node with their respective parents.
        """
        p_list = []
        p = self
        while type(p) != Null:
            p_list.append(p)
            p = p.parent()
        return [p.position() for p in reversed(p_list[:-1])]

    def ancestors(self) -> list[Node]:
        """
        List ancestors (parent, parent of parent, parent of parent of parent, ...).

        :return: Chain of ancestors that lead to this node, ordered ascending based on ``full_position()`` (document
            order).
        """
        ret = []
        parent_p = self.parent()
        while type(parent_p) != Null:
            ret.append(parent_p)
            parent_p = parent_p.parent()
        return ret

    def preceding(self) -> list[Node]:
        """
        List nodes preceding this node in the overall hierarchy, as if invoking ``descendants()`` on the root node and
        filtering such that only nodes before this node are returned.

        :return: Nodes preceding this node in the overall hierarchy, ordered ascending based on ``full_position()``
            (document order).
        """
        parent_p = self.parent()
        if type(parent_p) == Null:
            return []
        siblings = parent_p.children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[:self_idx_in_siblings]
        ret = parent_p.preceding() + [parent_p]
        for p in siblings:
            ret += [p]
            ret += p.descendants()
        return ret

    def preceding_sibling(self) -> list[Node]:
        """
        List sibling nodes preceding this node, as if invoking ``parent().children()`` and filtering such that only
        nodes before this node are returned.

        :return: Sibling nodes following this node in the overall hierarchy, ordered ascending based on
            ``full_position()`` (document order).
        """
        parent_p = self.parent()
        if type(parent_p) == Null:
            return []
        siblings = parent_p.children()
        self_idx_in_siblings = next(i for i, p in enumerate(siblings) if p.position() == self.position())
        siblings = siblings[:self_idx_in_siblings]
        return siblings

    def value(self) -> CoreTypeAlias | None:  # why None? In some cases, it'll have children but no value (no value = None, which is different from Null)
        """
        Get value.

        For a full discussion on the distinction between ``None`` and ``Null``, see this class's constructor.

        :return: Value of this node.
        """
        return self._value

    def label(self) -> str | int | float | bool | Null:
        """
        Get label of this node within its parent. Parents can have more than one node with the same label, meaning the
        label shouldn't be used as a unique identifier.

        :return: Label of this node within parent, or ``Null`` if this node has no parent (node is root).
        """
        if self._label is None:
            return Null()
        return self._label

    def full_label(self) -> list[str | int | float | bool]:
        """
        Get labels of nodes descending to this node, as if invoking ``label()`` on each element of
        ``ancestors()[1:] + [self]``.

        :return: Labels of ancestors and this node with their respective parents.
        """
        p_list = []
        p = self
        while type(p) != Null:
            p_list.append(p)
            p = p.parent()
        return [p.label() for p in reversed(p_list[:-1])]

    def to_dict(self) -> dict[str | int | float | bool | Null, tuple[CoreTypeAlias | None, dict]]:
        """
        Convert this node and its descendants into a dictionary. This method is typically used for adhoc debugging /
        testing purposes.

        :return: Dictionary representation of this node and its descendants. Keys are labels (which may not be unique)
            and values are a 2-tuple representing the scalar value and children.
        """
        ret = {}
        for pe in self.children():
            ret[pe.label()] = (pe.value(), pe.to_dict())
        return ret

    def __str__(self):
        return f'Node({self.full_label()}, {self.value()})'
