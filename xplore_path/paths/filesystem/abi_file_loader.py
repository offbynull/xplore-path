from __future__ import annotations

import json
import pathlib
import urllib
import urllib.parse
import urllib.request
from typing import Any

from xplore_path.paths.filesystem.abi_path import AbiRootPath, BASE_URL
from xplore_path.paths.filesystem.file_loader import FileLoader, PATH_LOADER


class AbiFileLoader(FileLoader):
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.abi'

    def path_creator(self, p: pathlib.Path) -> PATH_LOADER:
        return AbiRootPath

    def load(self, p: pathlib.Path) -> Any:
        codes = set(p.read_text(encoding='utf-8').split(' '))
        if codes != {''}:
            return codes
        params = {
            'criteria': 'model::Gene',
            'num_rows': 'all',
            'only': 'acronym',
        }
        query_url = f'{BASE_URL}?{urllib.parse.urlencode(params)}'
        with urllib.request.urlopen(query_url) as response:
            data = json.loads(response.read().decode())
            return {entry['acronym'] for entry in data['msg']}
