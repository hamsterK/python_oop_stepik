class AdvancedTuple(tuple):
    def __add__(self, other):
        return AdvancedTuple(tuple(self) + tuple(other))

    def __radd__(self, other):
        return AdvancedTuple(tuple(other) + tuple(self))


advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)
