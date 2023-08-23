"""
Реализуйте класс QuadraticPolynomial, описывающий квадратный трехчлен.
"""

import math


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def x2(self):
        discr = self._b ** 2 - 4 * self._a * self._c
        if discr >= 0:
            return (-self._b + math.sqrt(discr)) / (2 * self._a)
        return None

    @property
    def x1(self):
        discr = self._b ** 2 - 4 * self._a * self._c
        if discr >= 0:
            return (-self._b - math.sqrt(discr)) / (2 * self._a)
        return None

    @property
    def view(self):
        if self._c < 0:
            return f'{self._a}x^2 + {self._b}x - {abs(self._c)}'
        if self._b < 0:
            return f'{self._a}x^2 - {abs(self._b)}x + {self._c}'
        return f'{self._a}x^2 + {self._b}x + {self._c}'

    @property
    def coefficients(self):
        return self._a, self._b, self._c

    @coefficients.setter
    def coefficients(self, coef_tuple):
        self._a, self._b, self._c = coef_tuple


polynom = QuadraticPolynomial(1, 2, -3)

print(polynom.a)
print(polynom.b)
print(polynom.c)
