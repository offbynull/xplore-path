from math import isnan
from typing import TypeVar, Type, Any

from xplore_path.path import Path


T = TypeVar('T')


def coerce_single_value(v: Any, new_t: Type[T]) -> T | None:
    if type(v) == new_t:
        return v
    elif new_t == bool:
        if isinstance(v, Path):
            return coerce_single_value(v.value(), new_t)
        elif type(v) == bool:
            return v
        elif type(v) == str:
            return len(v) > 0
        elif type(v) == float:
            return not isnan(v) and v != 0
        elif type(v) == int:
            return v != 0
    elif new_t == int:
        if isinstance(v, Path):
            return coerce_single_value(v.value(), new_t)
        elif type(v) == bool:
            return int(v)
        elif type(v) == str:
            try:
                return int(v)
            except (ValueError, TypeError):
                ...
        elif type(v) == float and v.is_integer():
            return int(v)
        elif type(v) == int:
            return v
    elif new_t == float:
        if isinstance(v, Path):
            return coerce_single_value(v.value(), new_t)
        elif type(v) == bool:
            return float(v)
        elif type(v) == str:
            try:
                return float(v)
            except (ValueError, TypeError):
                ...
        elif type(v) == float:
            return v
        elif type(v) == int:
            return float(v)
    elif new_t == str:
        if isinstance(v, Path):
            return coerce_single_value(v.value(), new_t)
        elif type(v) == float and v.is_integer():
            return str(int(v))
        else:
            try:
                return str(v)
            except (ValueError, TypeError):
                ...
    return None