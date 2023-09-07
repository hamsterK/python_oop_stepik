class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __len__(self):
        return len(self.sequence)

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Индекс должен быть целым числом')
        if item < 0 or item >= len(self.sequence):
            raise IndexError('Неверный индекс')
        return self.sequence[len(self.sequence) - 1 - item]

    def __contains__(self, item):
        return item in self.sequence

    def __iter__(self):
        yield from reversed(self.sequence)


reversed_list = ReversedSequence([1, 2, 3, 4, 5])

print(reversed_list[0])
print(reversed_list[1])
print(reversed_list[2])
