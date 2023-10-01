import math


class Vector:
    def __init__(self, *args):
        self.points = args

    def __str__(self):
        return str(self.points)

    def __add__(self, other):
        if len(self.points) != len(other.points):
            raise ValueError('Векторы должны иметь равную длину')
        return Vector(*(i + j for i, j in zip(self.points, other.points)))

    def __sub__(self, other):
        if len(self.points) != len(other.points):
            raise ValueError('Векторы должны иметь равную длину')
        return Vector(*(i - j for i, j in zip(self.points, other.points)))

    def __mul__(self, other):
        if len(self.points) != len(other.points):
            raise ValueError('Векторы должны иметь равную длину')
        return  sum(i * j for i, j in zip(self.points, other.points))

    def __eq__(self, other):
        if len(self.points) != len(other.points):
            raise ValueError('Векторы должны иметь равную длину')
        return all(i == j for i, j in zip(self.points, other.points))

    def norm(self):
        squared_sum = sum(i ** 2 for i in self.points)
        return math.sqrt(squared_sum)


vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)
    