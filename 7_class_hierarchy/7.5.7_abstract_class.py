from collections.abc import Sequence


class DNA(Sequence):
    __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    def __init__(self, chain):
        self._chain = chain

    def __str__(self):
        return self._chain

    def __len__(self):
        return len(self._chain)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._chain[index], type(self).__BASE[self._chain[index]]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._chain == other._chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._chain + other._chain)
        return NotImplemented

    def __contains__(self, item):
        return item in self._chain


dna = DNA('TGAACCTGACCTCGATTTCAAGGG')

print(*dna)
print(*reversed(dna))
print('A' in dna)
print('C' not in dna)
