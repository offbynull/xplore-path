from __future__ import annotations

import hashlib
import pathlib
import pickle
import tarfile
import zipfile
from tempfile import TemporaryDirectory, gettempdir
from typing import Hashable

from xplore_path.paths.filesystem.combined_file_loader import CombinedFileLoader
from xplore_path.paths.filesystem.csv_file_loader import CsvFileLoader
from xplore_path.paths.filesystem.docx_file_loader import DocxFileLoader
from xplore_path.paths.filesystem.file_loader import FileLoader
from xplore_path.path.path import Path
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


class FileSystemPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            value: pathlib.Path,
            file_loader: FileLoader | None,
            workspace: pathlib.Path | None = None
    ):
        super().__init__(parent, label, value)
        if file_loader is None:
            file_loader = _DEFAULT_FILE_LOADER
        self.file_loader = file_loader
        if workspace is None:
            workspace = pathlib.Path(f'{gettempdir()}/xplore_path_cache').expanduser()
        self.workspace = workspace

    def all_children(self) -> list[Path]:
        ret = []
        path: pathlib.Path = self.value()
        for c in path.iterdir():
            c: pathlib.Path = c
            if c.is_file():
                c_stat = c.stat()
                cache_lookup_key = [str(c.absolute()), c_stat.st_mtime, c_stat.st_size]
                cache_lookup_key_bytes = pickle.dumps(cache_lookup_key)
                cache_lookup_key_hash = hashlib.sha256(cache_lookup_key_bytes).hexdigest()
                if self.file_loader.is_loadable(c):
                    cache_path = self.workspace / cache_lookup_key_hash
                    data = None
                    if cache_path.exists():
                        try:
                            data = pickle.loads(cache_path.read_bytes())
                        except Exception:
                            ...
                    if data is None:
                        data = self.file_loader.load(c)
                        cache_path.unlink(missing_ok=True)
                        cache_path.write_bytes(pickle.dumps(data))
                        # TODO: fsync to make sure its rewritten in the event of an OS crash?
                    ret.append(PythonObjectPath(self, c.name, data))
                elif c.suffix == '.zip':
                    cache_path = self.workspace / cache_lookup_key_hash
                    if not cache_path.exists():
                        intermediate_path = _temp_dir()
                        with zipfile.ZipFile(c, 'r') as f:
                            f.extractall(intermediate_path)
                        # TODO: before renaming, fsync to make sure its rewritten in the event of an OS crash?
                        intermediate_path.rename(cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.file_loader, self.workspace))
                elif c.suffix == '.tar':
                    cache_path = self.workspace / cache_lookup_key_hash
                    if not cache_path.exists():
                        intermediate_path = _temp_dir()
                        with tarfile.open(c, 'r') as f:
                            f.extractall(intermediate_path)
                        # TODO: before renaming, fsync to make sure its rewritten in the event of an OS crash?
                        intermediate_path.rename(cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.file_loader, self.workspace))
                elif c.suffixes[-2:] == ['.tar', '.gz']:
                    cache_path = self.workspace / cache_lookup_key_hash
                    if not cache_path.exists():
                        intermediate_path = _temp_dir()
                        with tarfile.open(c, 'r:gz') as f:
                            f.extractall(intermediate_path)
                        # TODO: before renaming, fsync to make sure its rewritten in the event of an OS crash?
                        intermediate_path.rename(cache_path)
                    ret.append(FileSystemPath(self, c.name, cache_path, self.file_loader, self.workspace))
                else:
                    ret.append(PythonObjectPath(self, c.name, None))
            elif c.is_dir():
                ret.append(FileSystemPath(self, c.name, c, self.file_loader, self.workspace))
        return ret

    @staticmethod
    def create_root_path(dir: pathlib.Path | str) -> FileSystemPath:
        if isinstance(dir, str):
            dir = pathlib.Path(dir).expanduser()
        if not dir.is_dir():
            raise ValueError('Must be a directory')
        return FileSystemPath(None, None, dir, None)


if __name__ == '__main__':
    path = FileSystemPath.create_root_path('~/')
    for inner_path in path.all_children():
        print(f'{inner_path}')
    print(f'{isinstance(path, Path)}')