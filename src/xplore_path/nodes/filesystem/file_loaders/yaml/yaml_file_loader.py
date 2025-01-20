from __future__ import annotations

import pathlib
from typing import Any

import yaml

from xplore_path.nodes.filesystem.file_loader import FileLoader


class YamlFileLoader(FileLoader):
    """
    ``FileLoader`` for YAML files.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix in {'.yaml', '.yml'}

    def load(self, p: pathlib.Path) -> Any:
        return yaml.safe_load(p.read_text())
