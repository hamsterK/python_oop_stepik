class ModularTuple(tuple):
    def __new__(cls, iterable=(), size=100, *args, **kwargs):
        iterable = map(lambda item: item % size, iterable)
        instance = super().__new__(cls, iterable)
        return instance


modulartuple = ModularTuple([101, 102, 103, 104, 105])

print(modulartuple)
print(type(modulartuple))
