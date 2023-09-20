from collections import UserList


class DefaultList(UserList):
    def __init__(self, iterable=(), default=None):
        super().__init__(item for item in iterable)
        self._default = default

    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return self._default


data = [1, 2, 3]
defaultlist = DefaultList(data)

print(defaultlist)
data.extend([4, 5, 6])
print(data)
print(defaultlist)
