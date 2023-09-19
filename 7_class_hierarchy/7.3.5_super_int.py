class SuperInt(int):
    def repeat(self, n=2):
        if self > 0:
            repeated_str = str(self) * n
        else:
            repeated_str = f'-{str(abs(self)) * abs(n)}'

        return SuperInt(int(repeated_str))

    def to_bin(self):
        if self == 0:
            return SuperInt(0)
        return SuperInt(bin(abs(int(self)))[2:]) if self >= 0 else SuperInt('-' + bin(abs(int(self)))[2:])

    def next(self):
        return SuperInt(int(self) + 1)

    def prev(self):
        return SuperInt(int(self) - 1)

    def __iter__(self):
        num_str = str(abs(self))
        return iter([SuperInt(int(digit)) for digit in num_str])


superint1 = SuperInt(1337)
superint2 = SuperInt(-2077)

print(*superint1)
print(*superint2)
