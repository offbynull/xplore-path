from __future__ import annotations

import pathlib
from enum import Enum
from tempfile import gettempdir
from typing import Callable
from weakref import WeakValueDictionary

from xplore_path.nodes.filesystem._cache import Cache
from xplore_path.nodes.filesystem.file_loader import FileLoader

from xplore_path.nodes.filesystem.file_loaders.allen_brain_institute_api.abi_file_loader import AbiFileLoader
from xplore_path.nodes.filesystem.file_loaders.combined.combined_file_loader import CombinedFileLoader
from xplore_path.nodes.filesystem.file_loaders.csv.csv_file_loader import CsvFileLoader
from xplore_path.nodes.filesystem.file_loaders.tsv.tsv_file_loader import TsvFileLoader
from xplore_path.nodes.filesystem.file_loaders.docx.docx_file_loader import DocxFileLoader
from xplore_path.nodes.filesystem.file_loaders.html.html_file_loader import HtmlFileLoader
from xplore_path.nodes.filesystem.file_loaders.json.json_file_loader import JsonFileLoader
from xplore_path.nodes.filesystem.file_loaders.pdf.pdf_file_loader import PdfFileLoader
from xplore_path.nodes.filesystem.file_loaders.sqlite.sqlite_file_loader import SqliteFileLoader
from xplore_path.nodes.filesystem.file_loaders.txt.text_file_loader import TextFileLoader
from xplore_path.nodes.filesystem.file_loaders.xlsx.xlsx_file_loader import XlsxFileLoader
from xplore_path.nodes.filesystem.file_loaders.xml.xml_file_loader import XmlFileLoader
from xplore_path.nodes.filesystem.file_loaders.yaml.yaml_file_loader import YamlFileLoader


_DEFAULT_FILE_LOADER = CombinedFileLoader([
    TextFileLoader(),
    JsonFileLoader(),
    YamlFileLoader(),
    PdfFileLoader(),
    CsvFileLoader(),
    TsvFileLoader(),
    XlsxFileLoader(),
    DocxFileLoader(),
    XmlFileLoader(),
    HtmlFileLoader(),
    SqliteFileLoader(),
    AbiFileLoader(),
    # DefaultFileLoader()
])


class NoticeType(Enum):
    """
    Event notice type.
    """
    DATA_CACHE_START = 'DATA_CACHE_START',
    """Notice that data caching has started."""
    DATA_CACHE_COMPLETE = 'DATA_CACHE_COMPLETE',
    """Notice that data caching has completed."""
    DATA_CACHE_ERROR = 'DATA_CACHE_ERROR',
    """Notice that data caching has failed."""
    DATA_LOAD_FULL_START = 'DATA_LOAD_FULL_START',
    """Notice that data loading has started."""
    DATA_LOAD_FULL_COMPLETE = 'DATA_LOAD_FULL_COMPLETE',
    """Notice that data loading has completed."""
    DATA_LOAD_FULL_ERROR = 'DATA_LOAD_FULL_ERROR',
    """Notice that data loading has failed."""
    DATA_LOAD_CACHE_START = 'DATA_LOAD_CACHE_START',
    """Notice that data loading (from cache) has started."""
    DATA_LOAD_CACHE_SUCCESS = 'DATA_LOAD_CACHE_COMPLETE',
    """Notice that data loading (from cache) has completed."""
    DATA_LOAD_CACHE_ABSENT = 'DATA_LOAD_CACHE_ERROR',
    """Notice that data loading (from cache) has failed."""
    ARCHIVE_CACHE_START = 'ARCHIVE_CACHE_START',
    """Notice that archive caching has started."""
    ARCHIVE_CACHE_COMPLETE = 'ARCHIVE_CACHE_COMPLETE',
    """Notice that archive caching has completed."""
    ARCHIVE_CACHE_ERROR = 'ARCHIVE_CACHE_ERROR'
    """Notice that archive caching has failed."""


class FileSystemContext:
    """
    ``FileSystemNode`` context.
    """
    def __init__(
            self,
            file_loader: FileLoader | None = None,
            workspace: pathlib.Path | None = None,
            cache_only_access: bool = False,
            cache_notifier: Callable[[NoticeType, pathlib.Path], None] | None = None
    ):
        """
        Construct a ``FileSystemContext`` object.

        :param file_loader: ``FileLoader`` to use when loading files (typically a ``CombinedFileLoader`` targeting many
            ``FileLoader``\s). If ``None``, uses default ``FileLoader``\s.
        :param workspace: Directory in which to store cache and temporary files. If ``None``, uses the
            `'xplore_path_cache'` subdirectory in the OS's temporary directory.
        :param cache_only_access: If ``True``, files are only ever loaded from cache, meaning that they aren't loaded if
            they haven't been cached beforehand. Otherwise, load from file if file is not cached.
        :param cache_notifier: Callback invoked to notify of data loading / caching events.  If ``None``, not invoked.
        """
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
