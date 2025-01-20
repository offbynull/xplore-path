from __future__ import annotations

import types
from typing import Any

from xplore_path.null import Null
from xplore_path.node import Node, ParentBlock


def _valid_obj_attr(obj, k):
    return not k.startswith('_') and \
        type(getattr(obj, k)) not in {str, int, float, bool, types.BuiltinFunctionType, types.BuiltinMethodType}


class PythonObjectNode(Node):
    """
    ``Node`` backed by a complex object. Best effort is made to represent the object graph as children, interpreting
    common collections (e.g. dict, list, tuple, etc...) and common built-in values.
    """
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            value: dict | set | list | tuple
    ):
        """
        Construct a ``PythonObjectNode`` object.

        :param parent: Attributes defining this node in relation to its parent, or ``None`` if this node has no parent
            (it represents root).
        :param value: Backing Python object.
        """
        if value is None:
            value = Null()
        super().__init__(parent, value if type(value) in {bool, int, float, str, Null} else None)
        self._data = value

    def children(self) -> list[Node]:
        this = self._data
        ret = []
        if isinstance(this, dict):
            for i, k in enumerate(this.keys()):
                ret += [PythonObjectNode(ParentBlock(self, i, k), this[k])]
        elif isinstance(this, set):
            for i, v in enumerate(this):
                return [PythonObjectNode(ParentBlock(self, i, i), v)]
        elif isinstance(this, (list, tuple)):
            for i, v in enumerate(this):
                ret += [PythonObjectNode(ParentBlock(self, i, i), v)]
        # Don't allow it to dive into Python objects - very expensive and not useful for now
        # for i, k in enumerate(k_ for k_ in dir(this) if _valid_obj_attr(this, k_)):
        #     ret += [PythonObjectPath(self, i, k, getattr(this, k))]
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> PythonObjectNode:
        """
        Equivalent to ``PythonObjectNode(None, obj)``.

        :param obj: Python object to represent as a ``Node``.
        :return: New ``PythonObjectNode``.
        """
        return PythonObjectNode(None, obj)


if __name__ == '__main__':
    x = { 1: 'z', 'a': { 'b': { 'c': 1, 'd': 2 } } }
    path = PythonObjectNode.create_root_path(x)
    for inner_path in path.descendants(max_depth=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Node)}')