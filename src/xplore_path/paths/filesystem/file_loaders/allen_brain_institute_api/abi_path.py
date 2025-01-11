from __future__ import annotations

import json
import urllib
import urllib.parse
import urllib.request

from xplore_path.path import Path
from xplore_path.paths.python_object.python_object_path import PythonObjectPath

BASE_URL = 'http://api.brain-map.org/api/v2/data/query.json'


class AbiAcronymPath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: str | int | float | bool | None,  # None for root
    ):
        super().__init__(parent, position_in_parent, label, None)

    def all_children(self) -> list[Path]:
        params = {
            'criteria': f'model::Gene[acronym$eq\'{self.label()}\']',
        }
        query_url = f'{BASE_URL}?{urllib.parse.urlencode(params)}'
        try:
            with urllib.request.urlopen(query_url) as response:
                data = json.loads(response.read().decode())
                if 'msg' in data:
                    return [PythonObjectPath(self, 0, 'data', data['msg'])]
                return []
        except Exception as e:
            return []


# http://api.brain-map.org/api/v2/data/query.json?criteria=model::Gene&num_rows=5&only=acronym"
# http://api.brain-map.org/api/v2/data/query.json?criteria=model::Gene[acronym$eq'A1BG']
class AbiRootPath(Path):
    def __init__(
            self,
            parent: Path | None,
            position_in_parent: int | None,
            label: str | int | float | bool | None,  # None for root
            codes: set[str]
    ):
        super().__init__(parent, position_in_parent, label, None)
        self.codes = codes

    def all_children(self) -> list[Path]:
        return [AbiAcronymPath(self, i, c) for i, c in enumerate(self.codes)]


if __name__ == '__main__':
    x = AbiRootPath(None, None, None, {'NAT2'})
    print(f'{x.all_descendants()}')