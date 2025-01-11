from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class IgnoreCaseMatcher(Matcher):
    def __init__(self, pattern: str):
        self.pattern = pattern

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        return value.casefold() == self.pattern.casefold()