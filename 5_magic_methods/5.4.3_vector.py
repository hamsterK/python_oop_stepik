from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __pos__(self):
        return Vector(self.x, self.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)
    