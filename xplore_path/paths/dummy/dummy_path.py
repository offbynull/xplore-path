from __future__ import annotations

from xplore_path.path import Path


class DummyPath(Path):
    def __init__(self):
        super().__init__(None, None, None, {})

    def all_children(self) -> list[Path]:
        return []


if __name__ == '__main__':
    path = DummyPath()
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')