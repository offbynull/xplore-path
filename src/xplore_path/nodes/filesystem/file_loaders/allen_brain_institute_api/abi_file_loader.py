from __future__ import annotations

import json
import pathlib
import urllib
import urllib.parse
import urllib.request
from typing import Any

from xplore_path.nodes.filesystem.file_loaders.allen_brain_institute_api._abi_node import AbiRootNode, BASE_URL
from xplore_path.nodes.filesystem.file_loader import FileLoader, NODE_CREATOR


class AbiFileLoader(FileLoader):
    """
    ``FileLoader`` that targets the Allen Brain Institute's API. This is a proof-of-concept, not intended for
    production use.
    """
    def is_loadable(self, p: pathlib.Path) -> bool:
        return p.suffix == '.abi'

    def node_creator(self, p: pathlib.Path) -> NODE_CREATOR:
        return AbiRootNode

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
