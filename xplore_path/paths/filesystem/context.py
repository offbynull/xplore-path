from __future__ import annotations

import pathlib
from enum import Enum
from tempfile import gettempdir
from typing import Callable
from weakref import WeakValueDictionary

from xplore_path.paths.filesystem.cache import Cache
from xplore_path.paths.filesystem.file_loader import FileLoader

from xplore_path.paths.filesystem.file_loaders.allen_brain_institute_api.abi_file_loader import AbiFileLoader
from xplore_path.paths.filesystem.file_loaders.combined.combined_file_loader import CombinedFileLoader
from xplore_path.paths.filesystem.file_loaders.csv.csv_file_loader import CsvFileLoader
from xplore_path.paths.filesystem.file_loaders.docx.docx_file_loader import DocxFileLoader
from xplore_path.paths.filesystem.file_loaders.html.html_file_loader import HtmlFileLoader
from xplore_path.paths.filesystem.file_loaders.json.json_file_loader import JsonFileLoader
from xplore_path.paths.filesystem.file_loaders.pdf.pdf_file_loader import PdfFileLoader
from xplore_path.paths.filesystem.file_loaders.sqlite.sqlite_file_loader import SqliteFileLoader
from xplore_path.paths.filesystem.file_loaders.txt.text_file_loader import TextFileLoader
from xplore_path.paths.filesystem.file_loaders.xlsx.xlsx_file_loader import XlsxFileLoader
from xplore_path.paths.filesystem.file_loaders.xml.xml_file_loader import XmlFileLoader
from xplore_path.paths.filesystem.file_loaders.yaml.yaml_file_loader import YamlFileLoader


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
    SqliteFileLoader(),
    AbiFileLoader(),
    # DefaultFileLoader()
])


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


class FileSystemContext:
    def __init__(
            self,
            file_loader: FileLoader | None = None,
            workspace: pathlib.Path | None = None,
            cache_only_access: bool = False,
            cache_notifier: Callable[[NoticeType, pathlib.Path], None] | None = None
    ):
        if file_loader is None:
            file_loader = _DEFAULT_FILE_LOADER
        self.file_loader = file_loader
        if workspace is None:
            workspace = pathlib.Path(f'{gettempdir()}/xplore_path_cache')
        self.cache = Cache(workspace)
        self.cache_only_access = cache_only_access
        if cache_notifier is None:
            cache_notifier = lambda _, __: None
        self.cache_notifier = cache_notifier
        self.mem_cache = WeakValueDictionary()
