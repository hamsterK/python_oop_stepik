class CyclicList:
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)
        self.iter_counter = 0

    def __len__(self):
        return len(self.iterable)

    def __iter__(self):
        while True:
            yield self.iterable[self.iter_counter]
            self.iter_counter = (self.iter_counter + 1) % len(self.iterable)

    def append(self, item):
        self.iterable.append(item)

    def pop(self, index=None):
        if index is None:
            index = len(self.iterable) - 1
        if index < 0 or index >= len(self.iterable):
            raise IndexError("Index out of range")
        return self.iterable.pop(index)

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if len(self.iterable) == 0:
            raise IndexError("CyclicList is empty")
        return self.iterable[index % len(self.iterable)]  # loop


cyclic_list = CyclicList([1, 2, 3])

cyclic_list.append(4)
print(cyclic_list.pop())  # Output: 4
print(len(cyclic_list))    # Output: 3
print(cyclic_list.pop(0))  # Output: 1
print(len(cyclic_list))    # Output: 2
