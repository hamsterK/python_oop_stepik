class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        self.a, self.b, self.c = side, side, side


triangle1 = Triangle(3, 4, 5)
triangle2 = EquilateralTriangle(3)

print(triangle1.perimeter())
print(triangle2.perimeter())
