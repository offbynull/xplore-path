from __future__ import annotations

import pathlib
from abc import ABC, abstractmethod
from typing import Any, Callable

from xplore_path.node import Node, ParentBlock
from xplore_path.nodes.python_object.python_object_node import PythonObjectNode


NODE_CREATOR = Callable[[ParentBlock | None, Any], Node]
"""
Type representing a function call that creates ``Node``\s. First argument is the ``Node``'s parent attributes (or
``None`` if the ``Node`` is root) and the 2nd argument is an arbitrary object representing data.
"""


class FileLoader(ABC):
    """
    A ``FileLoader`` loads a file as a ``Node``.
    """
    @abstractmethod
    def is_loadable(self, p: pathlib.Path) -> bool:
        """
        Check if file is loadable by this ``FileLoader``. This method typically inspects the file extension or magic
        bytes to determine if a file is of the expected type.

        :param p: File path.
        :return: ``True`` if loadable. Otherwise, ``False``.
        """
        ...

    def is_cachable(self, p: pathlib.Path) -> bool:
        """
        Check if file, once loaded as ``Node``, is allowed to be cached. Some loaded ``Node``\s end up accessing
        external resources (e.g. APIs), so caching may not be a good idea (data is not constant).

        :param p: File path.
        :return: ``True`` if cachable. Otherwise, ``False``.
        """
        return True

    def node_creator(self, p: pathlib.Path) -> NODE_CREATOR:
        """
        Get ``Node`` creator for this file type. ``load()``'s return value is typically passed into this creator to
        create a ``Node`` reflective of the loaded file's contents.

        :param p: File path.
        :return: ``Node`` creator.
        """
        return PythonObjectNode

    @abstractmethod
    def load(self, p: pathlib.Path) -> Any:
        """
        Load file, for ingestion into the 2nd parameter of the ``Callable`` returned by ``node_creator()``.

        :param p: File path.
        :return: ``p``'s content.
        """
        ...
