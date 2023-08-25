class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    @property
    def fields(self):
        return self.x, self.y

    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.fields == other.fields
        if isinstance(other, tuple):
            return self.fields == other
        return NotImplemented


a = Vector(1, 2)
pair1 = (1, 2)
pair2 = (3, 4)
pair3 = (5, 6, 7)
pair4 = (1, 2, 3, 4)
pair5 = (1, 4, 3, 2)

print(a == pair1)
print(a == pair2)
print(a == pair3)
print(a == pair4)
print(a == pair5)
