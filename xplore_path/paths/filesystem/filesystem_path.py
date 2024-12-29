from __future__ import annotations

import hashlib
import pathlib
import pickle
import tarfile
import zipfile
from enum import Enum
from tempfile import TemporaryDirectory, gettempdir
from typing import Hashable, Callable, Any
from weakref import WeakValueDictionary

from xplore_path.path.path import Path
from xplore_path.paths.filesystem.cache import Cache
from xplore_path.paths.filesystem.combined_file_loader import CombinedFileLoader
from xplore_path.paths.filesystem.csv_file_loader import CsvFileLoader
from xplore_path.paths.filesystem.docx_file_loader import DocxFileLoader
from xplore_path.paths.filesystem.file_loader import FileLoader
from xplore_path.paths.filesystem.html_file_loader import HtmlFileLoader
from xplore_path.paths.filesystem.json_file_loader import JsonFileLoader
from xplore_path.paths.filesystem.pdf_file_loader import PdfFileLoader
from xplore_path.paths.filesystem.text_file_loader import TextFileLoader
from xplore_path.paths.filesystem.xlsx_file_loader import XlsxFileLoader
from xplore_path.paths.filesystem.xml_file_loader import XmlFileLoader
from xplore_path.paths.filesystem.yaml_file_loader import YamlFileLoader
from xplore_path.paths.python_object.python_object_path import PythonObjectPath

_DEFAULT_FILE_LOADER = CombinedFileLoader([
    TextFileLoader(),
    JsonFileLoader(),
    YamlFileLoader(),
    PdfFileLoader(),
    CsvFileLoader(),
    XlsxFileLoader(),
    DocxFileLoader(),
    XmlFileLoader(),
    HtmlFileLoader(),
    # DefaultFileLoader()
])


def _temp_dir() -> pathlib.Path:
    return pathlib.Path(TemporaryDirectory(prefix='filesystem_path_intermediary', delete=False).name)


class NoticeType(Enum):
    DATA_CACHE_START = 'DATA_CACHE_START',
    DATA_CACHE_COMPLETE = 'DATA_CACHE_COMPLETE',
    DATA_CACHE_ERROR = 'DATA_CACHE_ERROR',
    DATA_LOAD_FULL_START = 'DATA_LOAD_FULL_START',
    DATA_LOAD_FULL_COMPLETE = 'DATA_LOAD_FULL_COMPLETE',
    DATA_LOAD_FULL_ERROR = 'DATA_LOAD_FULL_ERROR',
    DATA_LOAD_CACHE_START = 'DATA_LOAD_CACHE_START',
    DATA_LOAD_CACHE_SUCCESS = 'DATA_LOAD_CACHE_COMPLETE',
    DATA_LOAD_CACHE_ABSENT = 'DATA_LOAD_CACHE_ERROR',
    ARCHIVE_CACHE_START = 'ARCHIVE_CACHE_START',    
    ARCHIVE_CACHE_COMPLETE = 'ARCHIVE_CACHE_COMPLETE',    
    ARCHIVE_CACHE_ERROR = 'ARCHIVE_CACHE_ERROR'    


class FileSystemPathContext:
    def __init__(
            self,
            file_loader: FileLoader | None = None,
            workspace: pathlib.Path | None = None,
            cache_notifier: Callable[[NoticeType, pathlib.Path], None] | None = None
    ):
        if file_loader is None:
            file_loader = _DEFAULT_FILE_LOADER
        self.file_loader = file_loader
        if workspace is None:
            workspace = pathlib.Path(f'{gettempdir()}/xplore_path_cache').expanduser()
        self.cache = Cache(workspace)
        if cache_notifier is None:
            cache_notifier = lambda _: None
        self.cache_notifier = cache_notifier
        self.mem_cache = WeakValueDictionary()


class FileSystemPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: pathlib.Path,
            ctx: FileSystemPathContext
    ):
        super().__init__(parent, label, value)
        self.ctx = ctx

    def _notify(self, type_: NoticeType, path: pathlib.Path) -> None:
        try:
            self.ctx.cache_notifier(type_, path)
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

    def all_children(self) -> list[Path]:
        ret = []
        path: pathlib.Path = self.value()
        for c in path.iterdir():
            c: pathlib.Path = c
            if c.is_file():
                c_stat = c.stat()
                cache_lookup_key = [str(c.absolute()), c_stat.st_mtime, c_stat.st_size]
                if self.ctx.file_loader.is_loadable(c):
                    # try loading it from cache
                    self._notify(NoticeType.DATA_LOAD_CACHE_START, c)
                    data = self.ctx.cache.load(cache_lookup_key)
                    if data is None:
                        self._notify(NoticeType.DATA_LOAD_CACHE_ABSENT, c)
                    else:
                        self._notify(NoticeType.DATA_LOAD_CACHE_SUCCESS, c)
                    # if fail - try loading it directly
                    if data is None:
                        self._notify(NoticeType.DATA_LOAD_FULL_START, c)
                        try:
                            data = self.ctx.file_loader.load(c)
                            self._notify(NoticeType.DATA_LOAD_FULL_COMPLETE, c)
                        except Exception:
                            self._notify(NoticeType.DATA_LOAD_FULL_ERROR, c)
                        # its loaded now - put it in cache
                        if data is not None:
                            self._notify(NoticeType.DATA_CACHE_START, c)
                            self.ctx.cache.cache(cache_lookup_key, data)
                            # TODO: fsync to make sure its rewritten in the event of an OS crash?
                            self._notify(NoticeType.DATA_CACHE_COMPLETE, c)
                    # done
                    ret.append(PythonObjectPath(self, c.name, data))
                elif c.suffix == '.zip':
                    cache_path = self.ctx.cache.to_path(cache_lookup_key)
                    if not cache_path.exists():
                        self._unpack_archive(lambda c: zipfile.ZipFile(c, 'r'), c, cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.ctx))
                elif c.suffix == '.tar':
                    cache_path = self.ctx.cache.to_path(cache_lookup_key)
                    if not cache_path.exists():
                        self._unpack_archive(lambda c: tarfile.open(c, 'r'), c, cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.ctx))
                elif c.suffixes[-2:] == ['.tar', '.gz']:
                    cache_path = self.ctx.cache.to_path(cache_lookup_key)
                    if not cache_path.exists():
                        self._unpack_archive(lambda c: tarfile.open(c, 'r:gz'), c, cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.ctx))
                else:
                    ret.append(PythonObjectPath(self, c.name, None))
            elif c.is_dir():
                ret.append(FileSystemPath(self, c.name, c, self.ctx))
        return ret

    @staticmethod
    def create_root_path(
            dir: pathlib.Path | str,
            ctx: FileSystemPathContext | None = None
    ) -> FileSystemPath:
        if isinstance(dir, str):
            dir = pathlib.Path(dir).expanduser()
        if not dir.is_dir():
            raise ValueError('Must be a directory')
        if ctx is None:
            ctx = FileSystemPathContext()
        return FileSystemPath(None, None, dir, ctx)


if __name__ == '__main__':
    path = FileSystemPath.create_root_path('~/')
    for inner_path in path.all_children():
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')