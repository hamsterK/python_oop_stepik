class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    perimeter = property(get_perimeter)
    area = property(get_area)


rectangle = Rectangle(4, 5)

print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
