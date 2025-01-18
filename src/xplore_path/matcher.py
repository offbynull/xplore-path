"""Matcher scalar type."""

from __future__ import annotations

from abc import ABC, abstractmethod


class Matcher(ABC):
    """
    A matcher performs fuzzy / approximate matching on scalar data.
    """
    @abstractmethod
    def match(self, value: str | int | float | bool) -> bool:
        """
        Test ``value`` to see if it matches what this matcher is looking for.

        :param value: Value being matched.
        :return: ``True`` if ``value`` matched, ``False`` otherwise.
        """
        ...