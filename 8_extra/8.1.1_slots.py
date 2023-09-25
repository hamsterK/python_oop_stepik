from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')

    def __init__(self, name, color, area):
        self.name = name
        self.color = color
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, type(self)):
            return self.area < other.area
        return NotImplemented


print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
