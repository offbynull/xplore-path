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
        this = self.value()
        ret = []
        if isinstance(this, dict):
            for i, k in enumerate(this.keys()):
                ret += [PythonObjectPath(self, i, k, this[k])]
        elif isinstance(this, set):
            for i, v in enumerate(this):
                return [PythonObjectPath(self, i, i, v)]
        elif isinstance(this, (list, tuple)):
            for i, v in enumerate(this):
                ret += [PythonObjectPath(self, i, i, v)]
        # Don't allow it to dive into Python objects - very expensive and not useful for now
        # for i, k in enumerate(k_ for k_ in dir(this) if _valid_obj_attr(this, k_)):
        #     ret += [PythonObjectPath(self, i, k, getattr(this, k))]
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