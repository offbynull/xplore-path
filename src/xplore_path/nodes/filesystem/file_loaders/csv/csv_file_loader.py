from __future__ import annotations

import pathlib
from typing import Any

import pandas as pd

from xplore_path.nodes.filesystem.file_loader import FileLoader


class CsvFileLoader(FileLoader):
    """
    ``FileLoader`` for CSV files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.csv'

    def load(self, p: pathlib.Path) -> Any:
        return pd.read_csv(p, sep=None, engine='python').to_dict(orient='index')
