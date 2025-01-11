from __future__ import annotations

from math import isnan
from typing import Type, TypeAlias, Callable, TYPE_CHECKING

from xplore_path.invocable import Invocable
from xplore_path.matcher import Matcher
from xplore_path.path import Path
if TYPE_CHECKING:
    from xplore_path.collection import Collection


BasicType: TypeAlias = str | int | float | bool | Matcher | Invocable | Path


def _coerce_value(v: BasicType, new_t: Type[BasicType]) -> BasicType | None:
    if type(v) == new_t:
        return v
    elif new_t == bool:
        if isinstance(v, Path):
            return _coerce_value(v.value(), new_t)
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
            return _coerce_value(v.value(), new_t)
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
            return _coerce_value(v.value(), new_t)
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
            return _coerce_value(v.value(), new_t)
        elif type(v) == float and v.is_integer():
            return str(int(v))
        else:
            try:
                return str(v)
            except (ValueError, TypeError):
                ...
    return None


class Entity:
    def __init__(self, value: BasicType):
        self._value = value

    @property
    def value(self) -> BasicType:
        return self._value

    def depath(self) -> Entity:
        if isinstance(self._value, Path):
            return Entity(self._value.value())
        return self

    def invoke(self, args: list[Collection]) -> Collection | None:
        if isinstance(self.value, Invocable):
            try:
                return self.value.invoke(args)
            except Exception:
                ...  # do nothing
        return None

    def coerce(self, new_t: Type[BasicType]) -> Entity | None:
        new_value = _coerce_value(self._value, new_t)
        if new_value is None:
            return None
        return Entity(new_value)

    @staticmethod
    def coerce_to_matching(l_: Entity, r_: Entity) -> tuple[Entity, Entity] | tuple[None, None]:
        new_r_ = r_.coerce(type(l_.value))
        if new_r_ is not None:
            return l_, new_r_
        new_l_ = l_.coerce(type(r_.value))
        if new_l_ is not None:
            return new_l_, r_
        return None, None

    @staticmethod
    def apply_binary_boolean_op(
        l: Entity,
        r: Entity,
        test_op: Callable[[BasicType, BasicType], bool],
        required_type: Type | None
    ) -> Entity | None:
        # Paths to values (if they are paths)
        l = l.depath()
        r = r.depath()
        # Coerce to comparable types
        if required_type is not None:
            l = l.coerce(required_type)  # noqa
            r = r.coerce(required_type)  # noqa
        elif isinstance(l.value, Invocable) or isinstance(r.value, Invocable):
            l, r = None, None  # blank out if either is invocable
        elif isinstance(l.value, Path) or isinstance(r.value, Path):
            raise ValueError('This should never happen')  # depath'd above
        elif isinstance(l.value, Matcher) or isinstance(r.value, Matcher):
            ...  # skip coercion if either is a label matcher
        else:
            l, r = Entity.coerce_to_matching(l, r)  # coerce so that types match
        if l is None or r is None:
            return None
        return Entity(test_op(l.value, r.value))

    def __eq__(self, other):
        if isinstance(other, Entity) and self._value == other._value:
            return True
        if self._value == other:
            return True
        return False

    def __str__(self):
        return f'<entity>{self._value}'