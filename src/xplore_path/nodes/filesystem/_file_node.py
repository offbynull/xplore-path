from __future__ import annotations

import pathlib

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.filesystem.context import NoticeType, FileSystemContext
from xplore_path.nodes.mirror.mirror_node import MirrorNode


class FileNode(Node):
    def __init__(
            self,
            parent: ParentBlock | None,  # None for root
            fs_path: pathlib.Path,
            ctx: FileSystemContext
    ):
        super().__init__(parent, None)
        self._children = None
        self._ctx = ctx
        self._fs_path = fs_path

    def _notify(self, type_: NoticeType, path: pathlib.Path) -> None:
        try:
            self._ctx.cache_notifier(type_, path)
        except Exception:
            ...  # do nothing

    def children(self) -> list[Node]:
        if self._children is not None:
            return self._children
        c = self._fs_path
        c_stat = c.stat()
        cache_lookup_key = [str(c.absolute()), c_stat.st_mtime, c_stat.st_size]
        self._children = []
        if self._ctx.file_loader.is_loadable(c):
            # try loading it from cache
            self._notify(NoticeType.DATA_LOAD_CACHE_START, c)
            loaded, data = self._ctx.cache.load(cache_lookup_key)
            if loaded:
                self._notify(NoticeType.DATA_LOAD_CACHE_SUCCESS, c)
            else:
                self._notify(NoticeType.DATA_LOAD_CACHE_ABSENT, c)
            # if fail - try loading it directly - skip load+cache if cache only access
            if not loaded and not self._ctx.cache_only_access:
                self._notify(NoticeType.DATA_LOAD_FULL_START, c)
                try:
                    data = self._ctx.file_loader.load(c)
                    self._notify(NoticeType.DATA_LOAD_FULL_COMPLETE, c)
                except Exception:
                    self._notify(NoticeType.DATA_LOAD_FULL_ERROR, c)
                # data may failed to load - treat as loaded + cache anyways because it'll probably fail to load next time as well
                loaded = True
                if self._ctx.file_loader.is_cachable(c):
                    self._notify(NoticeType.DATA_CACHE_START, c)
                    self._ctx.cache.cache(cache_lookup_key, data)
                    # TODO: fsync to make sure its rewritten in the event of an OS crash?
                    self._notify(NoticeType.DATA_CACHE_COMPLETE, c)
            # done
            if loaded and data is not None:
                path_creator = self._ctx.file_loader.path_creator(c)
                path = path_creator(ParentBlock(self, 0, c.name), data)
                self._children = [MirrorNode(p, ParentBlock(self, i, p.label())) for i, p in enumerate(path.children())]
        return self._children