from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from xplore_path.path import Path, ParentBlock
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


@dataclass
class XmlTag:
    name: str
    attrs: dict[str, Any]
    text: str | None
    values: list[XmlTag]


class XmlObjectPath(Path):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            data: XmlTag
    ):
        super().__init__(parent, data.text if data.text is not None else None)
        self.data = data

    def all_children(self) -> list[Path]:
        ret = []
        i = 0
        for attr_name, attr in self.data.attrs.items():
            ret += [PythonObjectPath(ParentBlock(self, i, f'{attr_name}'), attr)]
            i += 1
        for tag in self.data.values:
            ret += [XmlObjectPath(ParentBlock(self, i, tag.name), tag)]
            i += 1
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> XmlObjectPath:
        return XmlObjectPath(None, obj)


if __name__ == '__main__':
    x = XmlTag('root', {'id': 'z'}, 'hi', [XmlTag('b', {}, 'bye', [])])
    path = XmlObjectPath.create_root_path(x)
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')