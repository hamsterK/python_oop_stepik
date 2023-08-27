from math import  sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __bool__(self):
        return any([self.x, self.y])

    def __int__(self):
        return int(sqrt(self.x ** 2 + self.y ** 2))

    def __float__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __complex__(self):
        return complex(self.x, self.y)


vector = Vector(3, 4)

print(vector)
print(int(vector))
print(float(vector))
print(complex(vector))
