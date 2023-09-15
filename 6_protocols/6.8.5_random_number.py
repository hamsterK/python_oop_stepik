import random


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        self.cache = cache
        self.value = random.randint(self.start, self.end)

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self.cache:
            return self.value
        return random.randint(self.start, self.end)

    def __set__(self, obj, value):
        raise AttributeError('Изменение невозможно')


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])
