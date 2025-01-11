import itertools
from enum import Enum
from itertools import product
from typing import Callable

from xplore_path.collection import Collection
from xplore_path.fallback_mode import FallbackMode
from xplore_path.collections.sequence_collection import SequenceCollection
from xplore_path.collections.single_value_collection import SingleValueCollection
from xplore_path.entity import Entity


class CombineMode(Enum):
    ZIP = 'ZIP'
    PRODUCT = 'PRODUCT'


class AggregateMode(Enum):
    ANY = 'ANY'
    ALL = 'ALL'
    NONE = 'NONE'


def combine_transform_aggregate(
        lhs: Collection,
        rhs: Collection,
        combine_mode: CombineMode,
        transformer: Callable[[int, Entity, int, Entity], Entity | None],
        transform_fallback_mode: FallbackMode,
        aggregate_mode: AggregateMode
) -> Collection:
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