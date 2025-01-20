from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


@dataclass
class XmlTag:
    name: str
    attrs: dict[str, Any]
    text: str | None
    values: list[XmlTag]


class XmlObjectNode(Node):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            data: XmlTag
    ):
        super().__init__(parent, data.text if data.text is not None else None)
        self.data = data

    def children(self) -> list[Node]:
        ret = []
        i = 0
        for attr_name, attr in self.data.attrs.items():
            ret += [PythonObjectNode(ParentBlock(self, i, f'{attr_name}'), attr)]
            i += 1
        for tag in self.data.values:
            ret += [XmlObjectNode(ParentBlock(self, i, tag.name), tag)]
            i += 1
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> XmlObjectNode:
        return XmlObjectNode(None, obj)


if __name__ == '__main__':
    x = XmlTag('root', {'id': 'z'}, 'hi', [XmlTag('b', {}, 'bye', [])])
    path = XmlObjectNode.create_root_path(x)
    for inner_path in path.descendants(max_depth=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Node)}')