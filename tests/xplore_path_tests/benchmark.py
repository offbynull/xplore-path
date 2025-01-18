import cProfile
import sys
from pathlib import Path

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.filesystem.context import FileSystemContext
from xplore_path.nodes.filesystem.filesystem_node import FileSystemNode

print("\n".join(sys.path))
print(Path.cwd().absolute())

profiler = cProfile.Profile()
profiler.enable()
try:
    fs_path = FileSystemNode.create_root_path(
        '~/Downloads',
        FileSystemContext(
            cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
        )
    )
    ret = Evaluator().evaluate(fs_path, "/mouse_assays.zip/Mouse_Assay_001.csv/0/Target_Gene_Protein[. = .]")
    #print(f'{len(ret)=}')
except KeyboardInterrupt:
    ...
profiler.disable()
profiler.print_stats(sort='time')