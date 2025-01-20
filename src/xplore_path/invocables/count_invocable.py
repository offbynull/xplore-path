from xplore_path.invocable import Invocable
from xplore_path.collection import Collection
from xplore_path.collections_.single_value_collection import SingleValueCollection


class CountInvocable(Invocable):
    """
    ```Invocable`` that returns the number of ``Entity``\s in a ``Collection``.
    """
    def invoke(self, args: list[Collection]) -> Collection:
        result, = args
        return SingleValueCollection(sum(1 for _ in result))