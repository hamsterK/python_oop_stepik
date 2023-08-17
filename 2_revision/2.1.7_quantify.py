"""
Функция quantify() должна считать, для скольких элементов итерируемого объекта iterable функция-предикат predicate
вернула значение True, и возвращать полученный результат.
"""


def quantify(iterable, predicate=None):
    counter = 0
    if predicate is None:
        predicate = bool
    for iter in iterable:
        if predicate(iter) is True:
            counter += 1
    return counter


iterable = iter(['', 1, 0, (), [[]], [], {1: 2}])

print(quantify(iterable, None))
