from __future__ import annotations

import types
from typing import Any, Hashable

from xplore_path.path.path import Path


class PythonObjectPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: Any
    ):
        super().__init__(parent, label, value)

    def all_children(self) -> list[Path]:
        parent = self.value()
        ret = []
        if isinstance(parent, dict):
            for k in parent.keys():
                ret += [PythonObjectPath(self, k, parent[k])]
        elif isinstance(parent, set):
            for k in parent:
                return [PythonObjectPath(self, k, k in parent)]
        elif isinstance(parent, (list, tuple)):
            for k in range(len(parent)):
                ret += [PythonObjectPath(self, k, parent[k])]
        for k in dir(parent):
            if k.startswith('_'):
                continue
            v = getattr(parent, k)
            if type(v) in {str, int, float, bool, types.BuiltinFunctionType, types.BuiltinMethodType}:
                continue
            ret += [PythonObjectPath(self, k, v)]
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> PythonObjectPath:
        return PythonObjectPath(None, None, obj)


if __name__ == '__main__':
    x = { 1: 'z', 'a': { 'b': { 'c': 1, 'd': 2 } } }
    path = PythonObjectPath.create_root_path(x)
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')