"""
Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность
ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1].
Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть
значение default.
"""


def pluck(data, path, default=None):
    keys = path.split('.')
    value = data
    for key in keys:
        if key in value:
            value = value[key]
        else:
            return default
    return value


d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))
