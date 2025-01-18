from __future__ import annotations

from typing import TypeAlias

from xplore_path.invocable import Invocable
from xplore_path.matcher import Matcher
from xplore_path.null import Null
from xplore_path.node import Node

CoreTypeAlias: TypeAlias = str | int | float | bool | Matcher | Invocable | Node | Null
