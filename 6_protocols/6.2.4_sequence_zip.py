import copy


class SequenceZip:
    def __init__(self, *args):
        new_args = copy.deepcopy(args)
        self.sequences = new_args

    def __len__(self):
        if not self.sequences:
            return 0
        min_len = min(len(seq) for seq in self.sequences)
        return min_len

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Index must be an integer')
        if not (0 <= item < len(self.sequences[0])):
            raise ValueError('Invalid index - out of range')
        return tuple(seq[item] for seq in self.sequences)

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]


x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
sequencezip = SequenceZip(x, y, z)

print(sequencezip[2])
x[-1], z[-1] = z[-1], x[-1]
print(sequencezip[2])
