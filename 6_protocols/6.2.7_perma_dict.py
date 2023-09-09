class PermaDict:
    def __init__(self, data=None):
        self.data = {} if data is None else data.copy()

    def keys(self):
        return self.data.keys()

    def values(self):
        return self.data.values()

    def items(self):
        return self.data.items()

    def __len__(self):
        return len(self.data)

    def __setitem__(self, key, value):
        if key in self.data:
            raise KeyError('Изменение значения по ключу невозможно')
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        return iter(self.data)


permadict = PermaDict({'name': 'Timur', 'city': 'Moscow', 'age': 30})

print(*permadict)
print(*permadict.keys())
print(*permadict.values())
print(*permadict.items())
