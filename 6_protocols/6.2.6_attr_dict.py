import copy


class AttrDict:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = copy.deepcopy(data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        yield from self.data

    def __getitem__(self, key):
        if key not in self.data:
            raise KeyError
        return self.data.get(key)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getattr__(self, name):
        if name not in self.data:
            raise KeyError
        return self.data.get(name)


d = AttrDict()
d.name = 'Leonardo da Vinci'

try:
    print(d['name'])
except KeyError:
    print('Ключ отсутствует')
    