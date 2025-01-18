import pathlib
from collections import defaultdict

from xplore_path.collection import Collection
from xplore_path.node import Node
from xplore_path.evaluator import _test_with_fs

import pandas as pd

from xplore_path.repl.outputter import Outputter


class CsvOutputter(Outputter):
    def extension(self) -> str:
        return 'csv'

    def output(self, collection: Collection, write_path: pathlib.Path):
        paths = list(collection.filter_unpacked(lambda _, v: isinstance(v, Node)).unpack)
        non_paths = list(collection.filter_unpacked(lambda _, v: not isinstance(v, Node)).unpack)

        path_labels_elem_cnt = max(len(p.full_label()) for p in paths)
        cut_idx = 0
        for cut_idx in range(0, path_labels_elem_cnt):
            row_distinct_cnt = len({tuple(p.full_label()[:cut_idx]) for p in paths})
            col_distinct_cnt = len({tuple(p.full_label()[cut_idx:]) for p in paths})
            if row_distinct_cnt > col_distinct_cnt:
                break

        data = defaultdict(lambda: [None] * len(paths))
        data_row_key_to_row_idx = {}
        for p in paths:
            label = tuple(p.full_label())
            col_key = label[cut_idx:]
            col_key_str = './' + '/'.join(f'{e}' for e in col_key)
            row_key = label[:cut_idx]
            row_key_str = './' + '/'.join(f'{e}' for e in row_key)
            if row_key not in data_row_key_to_row_idx:
                data_row_key_to_row_idx[row_key] = len(data_row_key_to_row_idx)
            row_idx = data_row_key_to_row_idx[row_key]
            data['__index__'][row_idx] = row_key_str
            if p.value() is not None:
                data[f'.{col_key_str}'][row_idx] = p.value()
        data['__extra__'] = non_paths

        # pad out so that all columns are of equal length, otherwise pandas will crash
        max_col_len = max(len(column) for column in data.values())
        for key in data:
            data[key] = data[key] + [None] * (max_col_len - len(data[key]))

        df = pd.DataFrame(data)
        df.to_csv(write_path)


if __name__ == '__main__':
    collection = _test_with_fs('~/Downloads', "/mouse_assays.zip/*[.//g'*Gene*' = g'*Cd40*']//*")
    file_path = pathlib.Path('~/output_test.csv').expanduser()
    CsvOutputter().output(collection, file_path)

    import platform
    import subprocess
    import os
    def open_file(file_path):
        system = platform.system()
        try:
            if system == "Windows":
                os.startfile(file_path)
            elif system == "Darwin":  # macOS
                subprocess.run(["open", file_path], check=True)
            else:  # Linux/Unix
                subprocess.run(["xdg-open", file_path], check=True)
        except FileNotFoundError:
            print(f"No associated application found to open {file_path}")
        except Exception as e:
            print(f"Error: {e}")

    open_file(file_path)




