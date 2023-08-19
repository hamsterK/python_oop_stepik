class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._update_perimeter_and_area()

    def _update_perimeter_and_area(self):
        self._perimeter = self._length * 2 + self._width * 2
        self._area = self._length * self._width

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def set_length(self, length):
        self._length = length
        self._update_perimeter_and_area()

    def set_width(self, width):
        self._width = width
        self._update_perimeter_and_area()

    perimeter = property(get_perimeter)
    area = property(get_area)

    length = property(lambda self: self._length, set_length)
    width = property(lambda self: self._width, set_width)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
