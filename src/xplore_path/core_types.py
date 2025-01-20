from __future__ import annotations

from typing import TypeAlias

from xplore_path.invocable import Invocable
from xplore_path.matcher import Matcher
from xplore_path.null import Null
from xplore_path.node import Node


CoreTypeAlias: TypeAlias = str | int | float | bool | Matcher | Invocable | Node | Null
"""
A type alias that covers all possible types supported by the system: Integer, float, string, bool, matcher, invocable,
etc... All types other than ``Node`` are considered as scalar types (not dividable into something smaller). ``Node`` is
not considered a scalar type because it's composed of other ``Node``\s.
"""
