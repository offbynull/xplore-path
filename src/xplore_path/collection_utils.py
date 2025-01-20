import itertools
from enum import Enum
from itertools import product
from typing import Callable

from xplore_path.collection import Collection
from xplore_path.fallback_mode import FallbackMode
from xplore_path.collections_.sequence_collection import SequenceCollection
from xplore_path.collections_.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity


class CombineMode(Enum):
    """
    Directive for how two ``Collection``\s are to have their entities paired up.
    """
    ZIP = 'ZIP'
    """``Collection``\s must zip their entities together, as if ``zip(a, b)``."""
    PRODUCT = 'PRODUCT'
    """``Collection``\s must cartesian product their entities together, as if ``itertools.product(a, b)``."""


class AggregateMode(Enum):
    """
    Directive for how the entities of a ``Collection`` are to be aggregated.
    """
    ANY = 'ANY'
    """``Collection`` must aggregate its entities such that it's ``True`` if any of its entities are ``True``."""
    ALL = 'ALL'
    """``Collection`` must aggregate its entities such that it's ``True`` if all of its entities are ``True``."""
    NONE = 'NONE'
    """``Collection`` must keep its entities as-is (no aggregation)."""


def combine_transform_aggregate(
        lhs: Collection,
        rhs: Collection,
        combine_mode: CombineMode,
        transformer: Callable[[int, Entity, int, Entity], Entity | None],
        transform_fallback_mode: FallbackMode,
        aggregate_mode: AggregateMode
) -> Collection:
    """
    Given two ``Collection``\s, pair their ``Entity``\s, transform those ``Entity`` pairs such that they're single, then
    aggregate those single results.

    :param lhs: ``Collection`` on the left-hand side.
    :param rhs: ``Collection`` on the right-hand side.
    :param combine_mode: Directive which defines how ``lhs`` and ``rhs``'s entities should be paired.
    :param transformer: ``Callable`` that transforms ``Entity`` pairs. The ``Callable`` takes 4 arguments:

        * Arguments 1 and 2 are an index within ``lhs`` and the ``Entity`` at that index, respective.
        * Arguments 3 amd 4 are an index within ``rhs`` and the ``Entity`` at that index, respective.

        Each invocation of the ``Callable`` transforms the input ``Entity``\s into a new output ``Entity``, or ``None``
        if there was a problem while transforming.
    :param transform_fallback_mode: Action to take when transformation fails (when an invocation of ``transformer``
        returns ``None``).
    :param aggregate_mode: Directive which defines how to aggregate the transformed entities.
    :return: ``lhs`` and ``rhs`` paired together, transformed, and aggregated. Note that the returned object will be a
        ``SingleValueCollection`` should either ...

          * ``lhs`` and ``rhs`` both be ``SingleValueCollection``\s,
          * or an aggregation other than ``AggregateMode.NONE`` is applied,
          * or both.

         Otherwise, the result will be a ``SequenceCollection``.
    """
    if combine_mode == CombineMode.ZIP:
        combiner = zip(enumerate(lhs), enumerate(rhs))
    elif combine_mode == CombineMode.PRODUCT:
        combiner = product(enumerate(lhs), enumerate(rhs))
    else:
        raise ValueError('This should never happen')

    if isinstance(lhs, SingleValueCollection) and isinstance(rhs, SingleValueCollection):
        ret = transform_fallback_mode.evaluate(transformer(0, lhs.single, 0, rhs.single))
        if ret:
            ret, = ret
            ret = SingleValueCollection(ret)
        else:
            ret = SequenceCollection.empty()
    else:
        ret = SequenceCollection.from_entities(
            itertools.chain(
                *(transform_fallback_mode.evaluate(transformer(li, lv, ri, rv)) for (li, lv), (ri, rv) in combiner)
            )
        )

    if aggregate_mode == AggregateMode.ALL:
        ret = SingleValueCollection(all(ret.unpack))
    elif aggregate_mode == AggregateMode.ANY:
        ret = SingleValueCollection(any(ret.unpack))
    elif aggregate_mode == AggregateMode.NONE:
        ...  # do nothing
    else:
        raise ValueError('This should never happen')

    return ret