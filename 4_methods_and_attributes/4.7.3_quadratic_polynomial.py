class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, elems):
        return cls(*elems)

    @classmethod
    def from_str(cls, elems):
        elems = [float(i) for i in elems.split(' ')]
        return cls(*elems)


polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
