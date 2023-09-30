from dataclasses import dataclass, field


@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

    def __post_init__(self):
        if self.x == 0.0 or self.y == 0:
            self.quadrant = 0
        elif self.x > 0 and self.y > 0:
            self.quadrant = 1
        elif self.x > 0 and self.y < 0:
            self.quadrant = 4
        elif self.x < 0 and self.y > 0:
            self.quadrant = 2
        else:
            self.quadrant = 3

    def symmetric_x(self):
        return Point(self.x, self.y * -1)

    def symmetric_y(self):
        return Point(self.x * -1, self.y)

    def __repr__(self):
        return f'Point(x={self.x}, y={self.y}, quadrant={self.quadrant})'


point = Point(1.0, 2.0)

print(point.symmetric_x())
print(point.symmetric_y())
