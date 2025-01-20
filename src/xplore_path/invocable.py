from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from xplore_path.collection import Collection


class Invocable(ABC):
    """
    An invocable performs some computation when invoked, as if invoking a function.
    """
    @abstractmethod
    def invoke(self, args: list[Collection]) -> Collection:
        """
        Invoke.

        :param args: Invocation arguments.
        :return: Invocation result.
        """
        pass