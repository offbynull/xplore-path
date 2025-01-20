from __future__ import annotations

import pathlib

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.filesystem._archive_node import ArchiveNode
from xplore_path.nodes.filesystem._file_node import FileNode
from xplore_path.nodes.filesystem.context import FileSystemContext


class FileSystemNode(Node):
    """
    ``Node`` backed by a directory. Children are child paths (directories and files) within backing the directory.
    If a supported file's type is recognized, that file is parsed and its data / structure is represented as the
    ``Node`` for that file.
    """
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            fs_path: pathlib.Path,
            ctx: FileSystemContext
    ):
        """
        Construct a ``FileSystemNode`` object.

        :param parent: Attributes defining this node in relation to its parent, or ``None`` if this node has no parent
            (it represents root).
        :param fs_path: Directory.
        :param ctx: Context.
        :raises ValueError: If ``fs_path`` is not a directory. The directory should be accessible throughout the entire
            lifetime of this object, otherwise the behavior of this object is undefined.
        """
        super().__init__(parent, None)
        self._ctx = ctx
        self._fs_path = fs_path
        if not self._fs_path.is_dir():
           raise ValueError('Directory expected')

    def children(self) -> list[Node]:
        if not self._fs_path.is_dir():
           raise ValueError('Directory expected')
        ret = []
        path: pathlib.Path = self._fs_path
        for c_idx, c in enumerate(sorted(path.iterdir())):
            c: pathlib.Path = c
            if c.is_file():
                if c.suffix in {'.zip', '.tar'} or  c.suffixes[-2:] == ['.tar', '.gz']:
                    ret.append(ArchiveNode(ParentBlock(self, c_idx, c.name), c, self._ctx, FileSystemNode))
                else:
                    ret.append(FileNode(ParentBlock(self, c_idx, c.name), c, self._ctx))
            elif c.is_dir():
                ret.append(FileSystemNode(ParentBlock(self, c_idx, c.name), c, self._ctx))
        return ret

    @staticmethod
    def create_root_path(
            dir: pathlib.Path | str,
            ctx: FileSystemContext | None = None
    ) -> FileSystemNode:
        if isinstance(dir, str):
            dir = pathlib.Path(dir).expanduser()
        if not dir.is_dir():
            raise ValueError('Must be a directory')
        if ctx is None:
            ctx = FileSystemContext()
        return FileSystemNode(None, dir, ctx)


if __name__ == '__main__':
    path = FileSystemNode.create_root_path('~/')
    for inner_path in path.children():
        print(f'{inner_path}')
    print(f'{isinstance(path, Node)}')