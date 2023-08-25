from functools import total_ordering


@total_ordering
class Month:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __str__(self):
        return f"{self.year}-{self.month}"

    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __eq__(self, other):
        if isinstance(other, Month):
            return self.month == other.month and self.year == other.year
        elif isinstance(other, tuple) and len(other) == 2:
            return self.month == other[1] and self.year == other[0]
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Month):
            return (self.month > other.month and self.year == other.year) or self.year > other.year
        elif isinstance(other, tuple) and len(other) == 2:
            return self.month > other[1] and self.year == other[0]
        return NotImplemented
    

print(Month(1999, 12) == Month(1999, 12))
print(Month(1999, 12) < Month(2000, 1))
print(Month(1999, 12) > Month(2000, 1))
print(Month(1999, 12) <= Month(1999, 12))
print(Month(1999, 12) >= Month(2000, 1))
