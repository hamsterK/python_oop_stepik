class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return SuperString(self.string * int(other))
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return SuperString(self.string[:len(self.string) // int(other)])
        return NotImplemented

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __rshift__(self, n):
        if isinstance(n, (int, float)):
            n = int(n)
            if n >= len(self.string):
                return SuperString("")
            return SuperString(self.string[n:])

        return NotImplemented

    def __rrshift__(self, other):
        return self.__lshift__(other)

    def __lshift__(self, n):
        if isinstance(n, (int, float)):
            n = int(n)
            if n >= len(self.string):
                return SuperString("")
            return SuperString(self.string[:len(self.string) - n])

        return NotImplemented

    def __rlshift__(self, other):
        return self.__rshift__(other)


s = SuperString('beegeek')
for i in range(9):
    print(f'{s} << {i} =', s << i)
    