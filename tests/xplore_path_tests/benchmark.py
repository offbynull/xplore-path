import cProfile
import sys
from pathlib import Path

from xplore_path.evaluator import Evaluator
from xplore_path.paths.filesystem.context import FileSystemContext
from xplore_path.paths.filesystem.filesystem_path import FileSystemPath

print("\n".join(sys.path))
print(Path.cwd().absolute())

profiler = cProfile.Profile()
profiler.enable()
try:
    fs_path = FileSystemPath.create_root_path(
        '~/Downloads',
        FileSystemContext(
            cache_notifier=lambda notice_type, real_path: print(f'{notice_type}: {real_path}')
        )
    )
    ret = Evaluator().evaluate(fs_path, "/mouse_assays.zip/*[.//g'*Gene*' = g'*Cd40*']")
    #print(f'{len(ret)=}')
except KeyboardInterrupt:
    ...
profiler.disable()
profiler.print_stats(sort='time')