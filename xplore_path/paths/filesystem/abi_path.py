from __future__ import annotations

import json
import urllib
import urllib.parse
import urllib.request
from typing import Hashable

from xplore_path.path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath


BASE_URL = 'http://api.brain-map.org/api/v2/data/query.json'


class AbiAcronymPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
    ):
        super().__init__(parent, label, None)

    def all_children(self) -> list[Path]:
        params = {
            'criteria': f'model::Gene[acronym$eq\'{self.label()}\']',
        }
        query_url = f'{BASE_URL}?{urllib.parse.urlencode(params)}'
        try:
            with urllib.request.urlopen(query_url) as response:
                data = json.loads(response.read().decode())
                if 'msg' in data:
                    return [PythonObjectPath(self, 'data', data['msg'])]
                return []
        except Exception as e:
            return []


# http://api.brain-map.org/api/v2/data/query.json?criteria=model::Gene&num_rows=5&only=acronym"
# http://api.brain-map.org/api/v2/data/query.json?criteria=model::Gene[acronym$eq'A1BG']
class AbiRootPath(Path):
    def __init__(
            self,
            parent: Path | None,
            label: Hashable | None,  # None for root - None is also a hashable type
            codes: set[str]
    ):
        super().__init__(parent, label, None)
        self.codes = codes

    def all_children(self) -> list[Path]:
        return [AbiAcronymPath(self, c) for c in self.codes]


if __name__ == '__main__':
    x = AbiRootPath(None, None, {'NAT2'})
    print(f'{x.all_descendants()}')