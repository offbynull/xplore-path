from __future__ import annotations

import pathlib
from typing import Any

import pandas as pd

from xplore_path.nodes.filesystem.file_loader import FileLoader


class XlsxFileLoader(FileLoader):
    """
    ``FileLoader`` for Microsoft Excel files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.xlsx'

    def load(self, p: pathlib.Path) -> Any:
        data = pd.read_excel(p, sheet_name=None)
        return {sheet: df.to_dict(orient='index') for sheet, df in data.items()}
