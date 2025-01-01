from __future__ import annotations

import types
from typing import Any, Hashable

from xplore_path.path import Path


def _valid_obj_attr(obj, k):
    return not k.startswith('_') and \
        type(getattr(obj, k)) not in {str, int, float, bool, types.BuiltinFunctionType, types.BuiltinMethodType}


class PythonObjectPath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: Any
    ):
        super().__init__(parent, position_in_parent, label, value)

    def all_children(self) -> list[Path]:
        parent = self.value()
        ret = []
        if isinstance(parent, dict):
            for i, k in enumerate(parent.keys()):
                ret += [PythonObjectPath(self, i, k, parent[k])]
        elif isinstance(parent, set):
            for i, v in enumerate(parent):
                return [PythonObjectPath(self, i, i, v)]
        elif isinstance(parent, (list, tuple)):
            for i, v in enumerate(parent):
                ret += [PythonObjectPath(self, i, i, v)]
        for i, k in enumerate(k_ for k_ in dir(parent) if _valid_obj_attr(parent, k_)):
            ret += [PythonObjectPath(self, i, k, getattr(parent, k))]
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> PythonObjectPath:
        return PythonObjectPath(None, None, None, obj)


if __name__ == '__main__':
    x = { 1: 'z', 'a': { 'b': { 'c': 1, 'd': 2 } } }
    path = PythonObjectPath.create_root_path(x)
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')