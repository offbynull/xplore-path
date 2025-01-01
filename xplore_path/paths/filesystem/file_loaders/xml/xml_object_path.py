from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Hashable

from xplore_path.path import Path
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
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            data: XmlTag
    ):
        super().__init__(parent, label, data.text if data.text is not None else None)
        self.data = data

    def all_children(self) -> list[Path]:
        ret = []
        for attr_name, attr in self.data.attrs.items():
            ret += [PythonObjectPath(self, f'{attr_name}', attr)]
        for tag in self.data.values:
            ret += [XmlObjectPath(self, tag.name, tag)]
        return ret

    @staticmethod
    def create_root_path(obj: Any) -> XmlObjectPath:
        return XmlObjectPath(None, None, obj)


if __name__ == '__main__':
    x = XmlTag('root', {'id': 'z'}, 'hi', [XmlTag('b', {}, 'bye', [])])
    path = XmlObjectPath.create_root_path(x)
    for inner_path in path.all_descendants(max_level=6):
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')