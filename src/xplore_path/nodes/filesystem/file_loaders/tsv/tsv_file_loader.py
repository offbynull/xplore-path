from __future__ import annotations

import pathlib
from typing import Any

import pandas as pd

from xplore_path.nodes.filesystem.file_loader import FileLoader


class TsvFileLoader(FileLoader):
    """
    ``FileLoader`` for TSV files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.tsv'

    def load(self, p: pathlib.Path) -> Any:
        return pd.read_csv(p, sep='\t', engine='python').to_dict(orient='index')
