from __future__ import annotations

import json
import pathlib
from typing import Any

from xplore_path.nodes.filesystem.file_loader import FileLoader


class JsonFileLoader(FileLoader):
    """
    ``FileLoader`` for JSON files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.json'

    def load(self, p: pathlib.Path) -> Any:
        return json.loads(p.read_text())
