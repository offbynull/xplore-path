from xplore_path.matcher import Matcher


class StrictMatcher(Matcher):
    def __init__(self, pattern: str | int | float | bool):
        self.pattern = pattern

    # MATCHES STRICTLY, WITHOUT COERCION
    def match(self, value: str | int | float | bool) -> bool:
        if type(self.pattern) in {int, float} and type(value) in {int, float}:
            return self.pattern == value  # special case - treat numbers as equal
        return type(value) == type(self.pattern) and self.pattern == value  # otherwise ensure types match
        # why is type test required? e.g. bool inherits from int