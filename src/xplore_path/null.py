"""Null scalar type."""


class Null:
    """
    Representation of an absent value, often represented as ``None``, ``null``, or ``nil`` in other languages / formats
    (e.g. ``None`` in Python). When a ``Node``'s value is set to ``Null()``, it often means the node exists but the
    scalar value it pointed to was explicitly set to absent.
    """
    def __hash__(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, Null)

    def __str__(self):
        return 'null'

    def __repr__(self):
        return 'null'