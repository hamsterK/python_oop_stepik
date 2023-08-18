from math import sqrt


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def abs(self):
        return sqrt(self.x ** 2 + self.y ** 2)
