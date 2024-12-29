from __future__ import annotations

import hashlib
import json
import pathlib
import pickle
import tarfile
import zipfile
from abc import ABC, abstractmethod
from tempfile import TemporaryDirectory, gettempdir
from typing import Hashable, Any
from xml.etree import ElementTree

import pandas as pd
import yaml
from PyPDF2 import PdfReader
from docx import Document

from xplore_path.path.path import Path
from xplore_path.paths.python_object_path import PythonObjectPath


class FileLoader(ABC):
    @abstractmethod
    def is_loadable(self, p: pathlib.Path) -> bool:
        ...

    @abstractmethod
    def load(self, p: pathlib.Path) -> Any:
        ...


class TextFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.txt'

    def load(self, p: pathlib.Path) -> Any:
        return p.read_text(encoding='utf-8')


class JsonFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.json'

    def load(self, p: pathlib.Path) -> Any:
        return json.loads(p.read_text())


class YamlFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix in {'.yaml', '.yml'}

    def load(self, p: pathlib.Path) -> Any:
        return yaml.safe_load(p.read_text())


class PdfFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.pdf'

    def load(self, p: pathlib.Path) -> Any:
        reader = PdfReader(p)
        return {reader.get_page_number(page): page.extract_text() for page in reader.pages}


class CsvFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.csv'

    def load(self, p: pathlib.Path) -> Any:
        return pd.read_csv(p, sep=None, engine='python').to_dict(orient='index')


class XlsxFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.xlsx'

    def load(self, p: pathlib.Path) -> Any:
        data = pd.read_excel(p)
        return {sheet: df.to_dict(orient='index') for sheet, df in data.items()}


class DocxFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.docx'

    def load(self, p: pathlib.Path) -> Any:
        doc = Document(str(p))
        return sum([paragraph.text for paragraph in doc.paragraphs], start='')


class XmlFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.xml'

    def load(self, p: pathlib.Path) -> Any:
        def xml_to_dict_with_attributes(element):
            node = {}
            for k, v in element.attrib.items():
                node[f'@{k}'] = v
            if list(element):
                node |= {i: {child.tag: xml_to_dict_with_attributes(child)} for i, child in enumerate(element)}
            elif element.text and element.text.strip():
                node['.text'] = element.text.strip()
            return node

        root = ElementTree.parse(p).getroot()
        return {root.tag: xml_to_dict_with_attributes(root)}


class DefaultFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return True

    def load(self, p: pathlib.Path) -> Any:
        try:
            return p.read_text(encoding='US-ASCII')
        except Exception:
            return {}


class CombinedFileLoader(FileLoader):
    def __init__(self, loaders: list[FileLoader]):
        self.loader = loaders

    def is_loadable(self, p: pathlib.Path) -> bool:
        return any(l.is_loadable(p) for l in self.loader)

    def load(self, p: pathlib.Path) -> Any:
        for l in self.loader:
            if l.is_loadable(p):
                try:
                    return l.load(p)
                except Exception:
                    ...
        return None


_DEFAULT_FILE_LOADER = CombinedFileLoader([
    TextFileLoader(),
    JsonFileLoader(),
    YamlFileLoader(),
    PdfFileLoader(),
    CsvFileLoader(),
    XlsxFileLoader(),
    DocxFileLoader(),
    XmlFileLoader(),
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