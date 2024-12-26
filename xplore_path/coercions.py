from abc import ABC
from math import isnan
from typing import ForwardRef, TypeVar, Type, Any, Literal, Hashable

from xplore_path.path import Path

LABEL_TYPE = str | int | float | bool
SINGLE_ENTRY_TYPE = str | int | float | bool | ForwardRef('label_matcher.label_matcher.Matcher')
ENTRY_TYPE = SINGLE_ENTRY_TYPE | list[SINGLE_ENTRY_TYPE]


T = TypeVar('T', bool, int, float, str)











def coerce_for_set_operation(value: Any) -> dict[tuple[Literal['PATH', 'RAW'], Hashable], Any]:
    value = coerce_to_list(value)
    ret = {}
    for v in value:
        if isinstance(v, Path):
            k = 'PATH', tuple(v.label())
        else:
            k = 'RAW', v
        try:
            ret[k] = v
        except TypeError:
            ...  # type is unhashable? silently discard it and move on
    return ret  # noqa


def coerce_to_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def coerce_to_single(value: Any) -> Any:
    if isinstance(value, list):
        if len(value) > 0:
            return value
        else:
            return None
    return value


def coerce_single_value(v: bool | int | float | str | Path, new_t: Type[T]) -> T | None:
    if type(v) == new_t:
        return v
    elif new_t == bool:
        if type(v) == Path:
            return coerce_single_value(v.last().value, new_t)
        elif type(v) == bool:
            return v
        elif type(v) == str:
            return len(v) > 0
        elif type(v) == float:
            return not isnan(v) and v != 0
        elif type(v) == int:
            return v != 0
    elif new_t == int:
        if type(v) == Path:
            return coerce_single_value(v.last().value, new_t)
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
        if type(v) == Path:
            return coerce_single_value(v.last().value, new_t)
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
        if type(v) == Path:
            return coerce_single_value(v.last().value, new_t)
        elif type(v) == float and v.is_integer():
            return str(int(v))
        else:
            try:
                return str(v)
            except (ValueError, TypeError):
                ...
    return None