from __future__ import annotations

from xplore_path.node import Node


class DummyNode(Node):
    def __init__(self):
        super().__init__(None, None)

    def children(self) -> list[Node]:
        return []


if __name__ == '__main__':
    path = DummyNode()
    for inner_path in path.descendants(max_depth=6):
        print(f'{inner_path}')