class SparseArray:
    def __init__(self, default):
        self.array = {}
        self.default = default

    def __len__(self):
        return len(self.array)

    def __getitem__(self, key):
        return self.array.get(key, self.default)

    def __setitem__(self, key, value):
        self.array[key] = value

    def __contains__(self, item):
        return item in self.array

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]


array = SparseArray(0)

array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])
