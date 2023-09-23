from collections.abc import *


class BitArray(Sequence):
    def __init__(self, iterable=[]):
        self.iterable = list(iterable)

    def __str__(self):
        return str(self.iterable)

    def __len__(self):
        return len(self.iterable)

    def __reversed__(self):
        return iter(reversed(self.iterable))

    def __iter__(self):
        yield from self.iterable

    def __getitem__(self, item):
        return self.iterable[item]

    def __invert__(self):
        inverted_bits = [1 - bit for bit in self.iterable]
        return BitArray(inverted_bits)

    def __contains__(self, item):
        return item in self.iterable

    def __and__(self, other):
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        result_bits = [bit1 & bit2 for bit1, bit2 in zip(self.iterable, other.iterable)]
        return BitArray(result_bits)

    def __or__(self, other):
        if not isinstance(other, BitArray) or len(self) != len(other):
            return NotImplemented
        result_bits = [bit1 | bit2 for bit1, bit2 in zip(self.iterable, other.iterable)]
        return BitArray(result_bits)


bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))
