import cProfile
import sys
from pathlib import Path

from xplore_path.evaluator import Evaluator
from xplore_path.nodes.filesystem.context import FileSystemContext
from xplore_path.nodes.filesystem.filesystem_node import FileSystemNode

print("\n".join(sys.path))
print(Path.cwd().absolute())

fs_path = FileSystemNode.create_root_path(
    '../../src/xplore_path',
    FileSystemContext(
        cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
    )
)
e = Evaluator()

profiler = cProfile.Profile()
profiler.enable()
try:
    ret = e.evaluate(fs_path, "/repl//*/body//Import//*")
finally:
    profiler.disable()
    profiler.print_stats(sort='tottime')
    print(f'{len(list(ret))=}')