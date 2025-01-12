class Null:
    def __hash__(self):
        return 0

    def __eq__(self, other):
        return isinstance(other, Null)

    def __str__(self):
        return 'null'

    def __repr__(self):
        return 'null'