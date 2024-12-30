from __future__ import annotations

import types
from typing import Any, Hashable

from xplore_path.path.path import Path


class HtmlObjectPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            data: dict[Any, Any]
    ):
        super().__init__(parent, label, data['.text'] if isinstance(data, dict) and '.text' in data else data)
        self.data = data

    def all_children(self) -> list[Path]:
        ret = []
        if isinstance(self.data, dict):
            for k in self.data.keys():
                if k == '.text':
                    continue
                ret += [HtmlObjectPath(self, k, self.data[k])]
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> HtmlObjectPath:
        return HtmlObjectPath(None, None, obj)


if __name__ == '__main__':
    x = { 1: 'z', '.text': 'hi', 'a': { 'b': { '.text': 'bye', 'c': 1, 'd': 2 } } }
    path = HtmlObjectPath.create_root_path(x)
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')