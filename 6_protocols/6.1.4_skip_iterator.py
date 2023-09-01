class SkipIterator:
    def __init__(self, iterable, n):
        self.iterable = iter(iterable)
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        next_elem = next(self.iterable)
        while self.count < self.n:
            self.count += 1
            try:
                next(self.iterable)
            except StopIteration:
                return next_elem
        self.count = 0
        return next_elem


skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)

print(*skipiterator)
