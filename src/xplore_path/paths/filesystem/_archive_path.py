from __future__ import annotations

import pathlib
import tarfile
import zipfile
from tempfile import TemporaryDirectory
from typing import Any, Callable

from xplore_path.path import Path
from xplore_path.paths.filesystem._file_path import FilePath
from xplore_path.paths.filesystem.context import NoticeType, FileSystemContext


def _temp_dir() -> pathlib.Path:
    return pathlib.Path(TemporaryDirectory(prefix='filesystem_path_intermediary', delete=False).name)


class ArchivePath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: str | int | float | bool | None,  # None for root
            fs_path: pathlib.Path,
            ctx: FileSystemContext,
            fspath_creator: Callable  # Required to avoid cyclical import
    ):
        super().__init__(parent, position_in_parent, label, None)
        self._children = None
        self._ctx = ctx
        self._fspath_creator = fspath_creator
        self._fs_path = fs_path

    def _notify(self, type_: NoticeType, path: pathlib.Path) -> None:
        try:
            self._ctx.cache_notifier(type_, path)
        except Exception:
            ...  # do nothing

    def _unpack_archive(
            self,
            open_func: Callable[[pathlib.Path], Any],
            real_path: pathlib.Path,
            cache_path: pathlib.Path
    ) -> None:
        self._notify(NoticeType.ARCHIVE_CACHE_START, real_path)
        intermediate_path = _temp_dir()
        try:
            with open_func(real_path) as f:
                f.extractall(intermediate_path)
            # TODO: before renaming, fsync to make sure its rewritten in the event of an OS crash?
            intermediate_path.rename(cache_path)  # assume this is atomic operation
            self._notify(NoticeType.ARCHIVE_CACHE_COMPLETE, real_path)
        except Exception:
            self._notify(NoticeType.ARCHIVE_CACHE_ERROR, real_path)

    def _create_children(self, cache_path):
        for c_idx, c in enumerate(sorted(cache_path.iterdir())):
            if c.is_dir():
                self._children.append(self._fspath_creator(self, c_idx, c.name, c, self._ctx))
            else:
                self._children.append(FilePath(self, c_idx, c.name, c, self._ctx))

    def all_children(self) -> list[Path]:
        if self._children is not None:
            return self._children
        self._children = []
        c = self._fs_path
        c_stat = c.stat()
        cache_lookup_key = [str(c.absolute()), c_stat.st_mtime, c_stat.st_size]
        if c.suffix == '.zip':  # skip it if set to only access cached
            cache_path = self._ctx.cache.to_path(cache_lookup_key)
            if not cache_path.exists() and not self._ctx.cache_only_access:  # skip unpack if cache only access
                self._unpack_archive(lambda c: zipfile.ZipFile(c, 'r'), c, cache_path)
            self._create_children(cache_path)
        elif c.suffix == '.tar':  # skip it if set to only access cached
            cache_path = self._ctx.cache.to_path(cache_lookup_key)
            if not cache_path.exists() and not self._ctx.cache_only_access:  # skip unpack if cache only access
                self._unpack_archive(lambda c: tarfile.open(c, 'r'), c, cache_path)
            self._create_children(cache_path)
        elif c.suffixes[-2:] == ['.tar', '.gz']:
            cache_path = self._ctx.cache.to_path(cache_lookup_key)
            if not cache_path.exists() and not self._ctx.cache_only_access:  # skip unpack if cache only access
                self._unpack_archive(lambda c: tarfile.open(c, 'r:gz'), c, cache_path)
            self._create_children(cache_path)
        return self._children