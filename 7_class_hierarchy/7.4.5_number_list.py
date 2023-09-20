from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable=()):
        if not all(isinstance(i, (int, float)) for i in iterable):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__init__(iterable)

    def __setitem__(self, index, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__setitem__(index, item)

    def insert(self, index, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().insert(index, item)

    def append(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().append(item)

    def extend(self, other):
        if not all(isinstance(i, (int, float)) for i in other):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().extend(other)

    def __iadd__(self, other):
        if not all(isinstance(i, (int, float)) for i in other):
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
        super().__iadd__(other)
        return self


numberlist = NumberList([1, 2])

try:
    numberlist += [3, '4']
except TypeError as e:
    print(e)
