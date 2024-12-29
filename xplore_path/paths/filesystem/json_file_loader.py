from __future__ import annotations

import json
import pathlib
from typing import Any

from xplore_path.paths.filesystem.file_loader import FileLoader


class JsonFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.json'

    def load(self, p: pathlib.Path) -> Any:
        return json.loads(p.read_text())
