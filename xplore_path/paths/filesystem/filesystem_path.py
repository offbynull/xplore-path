from __future__ import annotations

import pathlib
from typing import Hashable

from xplore_path.path import Path
from xplore_path.paths.filesystem.context import FileSystemContext
from xplore_path.paths.filesystem._archive_path import ArchivePath
from xplore_path.paths.filesystem._file_path import FilePath


class FileSystemPath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: pathlib.Path,
            ctx: FileSystemContext
    ):
        super().__init__(parent, position_in_parent, label, value)
        self._ctx = ctx

    def all_children(self) -> list[Path]:
        if not self.value().is_dir():
           raise ValueError('Directory expected')
        ret = []
        path: pathlib.Path = self.value()
        for c_idx, c in enumerate(sorted(path.iterdir())):
            c: pathlib.Path = c
            if c.is_file():
                if c.suffix in {'.zip', '.tar'} or  c.suffixes[-2:] == ['.tar', '.gz']:
                    ret.append(ArchivePath(self, c_idx, c.name, c, self._ctx, FileSystemPath))
                else:
                    ret.append(FilePath(self, c_idx, c.name, c, self._ctx))
            elif c.is_dir():
                ret.append(FileSystemPath(self, c_idx, c.name, c, self._ctx))
        return ret

    @staticmethod
    def create_root_path(
            dir: pathlib.Path | str,
            ctx: FileSystemContext | None = None
    ) -> FileSystemPath:
        if isinstance(dir, str):
            dir = pathlib.Path(dir).expanduser()
        if not dir.is_dir():
            raise ValueError('Must be a directory')
        if ctx is None:
            ctx = FileSystemContext()
        return FileSystemPath(None, None, None, dir, ctx)


if __name__ == '__main__':
    path = FileSystemPath.create_root_path('~/')
    for inner_path in path.all_children():
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')