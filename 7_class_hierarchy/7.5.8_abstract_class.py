from collections.abc import MutableSequence


class SortedList(MutableSequence):
    def __init__(self, iterable=None):
        if iterable is None:
            self.data = []
        else:
            self.data = sorted(iterable)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return SortedList(self.data[index])
        return self.data[index]

    def __setitem__(self, key, value):
        raise NotImplementedError("Setting an item is not supported")

    def __delitem__(self, key):
        del self.data[key]

    def add(self, item):
        self.data.append(item)
        self.data.sort()

    def discard(self, item):
        while item in self.data:
            self.data.remove(item)

    def update(self, iterable):
        self.data.extend(iterable)
        self.data.sort()

    def append(self, item):
        raise NotImplementedError("Append is not supported")

    def insert(self, index, value):
        raise NotImplementedError("Insert is not supported")

    def extend(self, iterable):
        raise NotImplementedError("Extend is not supported")

    def reverse(self):
        raise NotImplementedError("Reverse is not supported")

    def __repr__(self):
        return f"SortedList({self.data})"

    def __len__(self):
        return len(self.data)

    def __reversed__(self):
        raise NotImplementedError("Reversed is not supported")

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return item in self.data

    def __add__(self, other):
        if isinstance(other, SortedList):
            return SortedList(self.data + other.data)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, SortedList):
            self.data.extend(other.data)
            self.data.sort()
            return self
        else:
            return NotImplemented

    def __mul__(self, n):
        if isinstance(n, int):
            return SortedList(self.data * n)
        else:
            return NotImplemented

    def __imul__(self, n):
        if isinstance(n, int):
            self.data *= n
            self.data.sort()
            return self
        else:
            return NotImplemented


numbers1 = SortedList([1, 3, 5])
numbers2 = SortedList([2, 4])

id1_numbers1 = id(numbers1)
id1_numbers2 = id(numbers2)

numbers1 += numbers2
numbers2 *= 2

id2_numbers1 = id(numbers1)
id2_numbers2 = id(numbers2)

print(id1_numbers1 == id2_numbers1)
print(id1_numbers2 == id2_numbers2)
print(3 in numbers1)
