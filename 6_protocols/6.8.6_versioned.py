class Versioned:
    def __init__(self):
        self._index = -1

    def __set_name__(self, owner, name):
        self._attr = name

    def __get__(self, obj, owner):
        if obj is None:
            return self
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr][self._index]
        raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        if self._attr not in obj.__dict__:
            obj.__dict__[self._attr] = []
        obj.__dict__[self._attr].append(value)

    def get_version(self, obj, n):
        return obj.__dict__[self._attr][n - 1]

    def set_version(self, obj, n):
        self._index = n - 1