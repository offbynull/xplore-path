from xplore_path.entity import Entity
from xplore_path.matcher import Matcher


class AcronymMatcher(Matcher):
    """
    ``Matcher`` that attempts to pull out and match against an acronym from a snake-case, camel-case, or title-case
    string. If value isn't a string, it's coerced into one prior to testing for a match.
    """
    def __init__(self, pattern: str):
        """
        Construct a ``AcronymMatcher`` object.

        :param pattern: Acronym to test against.
        """
        self._pattern = pattern

    def match(self, value: str | int | float | bool) -> bool:
        value = Entity(value).coerce(str)
        if value is None:
            return False
        value = value.value
        acronyms = [
            AcronymMatcher._snakecase_extract(value),
            AcronymMatcher._titlecase_extract(value),
            AcronymMatcher._camelcase_extract(value)
        ]
        acronyms = [a for a in acronyms if a is not None]
        if not acronyms:
            return False
        acronym = max(acronyms, key=lambda a: len(a))
        return acronym == self._pattern

    @staticmethod
    def _snakecase_extract(val: str) -> str | None:
        ret = ''
        current_word = ''
        for v in val:
            if v == '_':
                if current_word == '' or not current_word.isalnum():
                    return None
                ret += current_word[0]
                current_word = ''
            elif v.isalnum() and v.islower():
                current_word += v
            else:
                return None
        if current_word and current_word.isalnum():
            ret += current_word[0]
        return ret

    @staticmethod
    def _titlecase_extract(val: str) -> str | None:
        val_it = iter(val)
        ret = ''
        current_word = next(val_it, None)
        if current_word is None or not (current_word.isalnum() and current_word.isupper()):
            return None
        for v in val_it:
            if v.isupper():
                if current_word == '' or not current_word.isalnum():
                    return None
                ret += current_word[0]
                current_word = v
            elif v.isalnum():
                current_word += v
            else:
                return None
        if current_word and current_word.isalnum():
            ret += current_word[0]
        return ret

    @staticmethod
    def _camelcase_extract(val: str) -> str | None:
        val_it = iter(val)
        ret = ''
        current_word = next(val_it, None)
        if current_word is None or not (current_word.isalnum() and current_word.islower()):
            return None
        for v in val_it:
            if v.isupper():
                if current_word == '' or not current_word.isalnum():
                    return None
                ret += current_word[0]
                current_word = v
            elif v.isalnum():
                current_word += v
            else:
                return None
        if current_word and current_word.isalnum():
            ret += current_word[0]
        return ret