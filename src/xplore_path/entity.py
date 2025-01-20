from __future__ import annotations

from math import isnan
from typing import Type, Callable, TYPE_CHECKING

from xplore_path.core_types import CoreTypeAlias
from xplore_path.invocable import Invocable
from xplore_path.matcher import Matcher
from xplore_path.node import Node
if TYPE_CHECKING:
    from xplore_path.collection import Collection


def _coerce_value(v: CoreTypeAlias, new_t: Type[CoreTypeAlias]) -> CoreTypeAlias | None:
    if type(v) == new_t:
        return v
    elif new_t == bool:
        if isinstance(v, Node):
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
        if isinstance(v, Node):
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
        if isinstance(v, Node):
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
        if isinstance(v, Node):
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
    """
    ``Entity`` wraps an object of a core type (see ``CoreTypeAlias``), providing helper / utility functionality.
    """

    def __init__(self, value: CoreTypeAlias):
        """
        Construct an ``Entity`` object.

        :param value: Value to wrap.
        """
        self._value = value

    @property
    def value(self) -> CoreTypeAlias:
        """
        Get wrapped value.

        :return: Value.
        """
        return self._value

    def denode(self) -> Entity | None:
        """
        Get the wrapped ``Node``'s value wrapped as an ``Entity``, assuming the wrapped value is actually a ``Node``.
        That is, if the wrapped value ...

         * is a ``Node`` and it has a non-``None`` value, return that value as an ``Entity``.
         * is a ``Node`` and it has a ``None` value, return ``None``.
         * isn't a ``Node``, return ``self``.

        The intent of this function is to streamline access to the values in a collection of ``Entity``\s. That is,
        certain operations don't consider a ``Node`` itself as a value, but the value within that ``Node``. For example,
        consider summing ...

        * a ``Node`` with an ``int``: Chances are you want to sum the value within that ``Node`` with the integer.
        * an ``int`` with a ``Node``: Chances are you want to sum the integer with the value within that ``Node``.
        * a ``Node`` with a ``Node``: Chances are you want to sum the values within those two ``Node``\s.

        :return: Wrapped ``Node``'s value as an ``Entity``, or ``self`` if wrapped value isn't a ``Node``.
        """
        if isinstance(self._value, Node):
            v = self._value.value()
            if v is None:
                return None
            return Entity(v)
        return self

    def invoke(self, args: list[Collection]) -> Collection | None:
        """
        Invoke the wrapped ``Invocable``, assuming the wrapped value actually is an ``Invocable``. If the wrapped value
        isn't an ``Invocable``, does nothing.

        :param args: Arguments to pass into the wrapped ``Invocable``'s invocation.
        :return: Result of the wrapped ``Invocable``'s invocation, or ``None`` if the wrapped value isn't an
            ``Invocable``.
        """
        if isinstance(self.value, Invocable):
            try:
                return self.value.invoke(args)
            except Exception:
                ...  # do nothing
        return None

    def coerce(self, new_t: Type[CoreTypeAlias]) -> Entity | None:
        """
        Coerce the wrapped value to another type.

        :param new_t: Type to coerce to.
        :return: An ``Entity`` wrapping ``self``'s value coerced to type ``new_t``, or ``None`` if ``self``'s value
            isn't coercible to type ``new_t``.
        """
        new_value = _coerce_value(self._value, new_t)
        if new_value is None:
            return None
        return Entity(new_value)

    @staticmethod
    def coerce_to_matching(l_: Entity, r_: Entity) -> tuple[Entity, Entity] | tuple[None, None]:
        """
        Coerce ``l_`` and ``r_`` such that their respective wrapped values are of the same type.

        :param l_: Entity whose wrapped value to coerce.
        :param r_: Entity whose wrapped value to coerce.
        :return: ``l_`` and ``r_`` with their wrapped values coerced such that they're of the same type, or the 2-tuple
            ``None, None`` if no such coercion is possible.
        """
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
        test_op: Callable[[CoreTypeAlias, CoreTypeAlias], bool],
        required_type: Type[CoreTypeAlias] | None
    ) -> Entity | None:
        """
        Apply a boolean operator on two ``Entity``\s. This function massages the operands ``l`` and ``r`` before passing
        them into the operator ``test_op`` as unwrapped values (unwrapped as in passing the ``Entity``'s wrapped value
        as opposed to the ``Entity`` itself). Specifically, ``l`` and ``r`` either ...

         * get coerced to ``required_type``, if ``required_type`` is not ``None``.
         * get coerced to have matching types, if ``required_type`` is ``None``.

        If coercion fails, the invocation of ``test_op`` is skipped and instead ``None`` is returned. In certain cases,
        no coercion is performed. For example, when comparing something to a ``Matcher``, it doesn't make much sense to
        attempt coercion on the opposing value as it's expected that the ``Matcher`` itself coerces the opposing value
        during its matching process (only if it deems in necessary - it doesn't have to coerce).

        :param l: ``Entity`` representing the left-hand side of the operator.
        :param r: ``Entity`` representing the right-hand side of the operator.
        :param test_op: Operator - function that takes in the wrapped values within ``l`` and ``r`` and spits out a
            boolean.
        :param required_type: Operand type required by ``test_op``.
        :return: The result of ``test_op(l, r)``, assuming that ``l`` and ``r`` were coerced for ingestion into
            ``test_op``. That is
        """
        # Nodes to values (if they're nodes)
        l = l.denode()
        r = r.denode()
        if l is None or r is None:  # It was a node, but node had no value assigned to it
            return None
        # Coerce to comparable types
        if required_type is not None:
            l = l.coerce(required_type)
            r = r.coerce(required_type)
        # elif isinstance(l.value, Invocable) or isinstance(r.value, Invocable):
        #     l, r = None, None  # Blank out if either is invocable
        elif isinstance(l.value, Node) or isinstance(r.value, Node):
            raise ValueError('This should never happen')  # Should have been denode'd above
        elif isinstance(l.value, Matcher) or isinstance(r.value, Matcher):
            ...  # Skip coercion if either is a matcher
        else:
            l, r = Entity.coerce_to_matching(l, r)  # Coerce so that types match
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
        return f'Entity({type(self._value)}{self._value})'