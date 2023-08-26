class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __add__(self, other):
        if not isinstance(other, FoodInfo):
            return NotImplemented
        return FoodInfo(self.proteins + other.proteins, self.fats + other.fats,
                        self.carbohydrates + other.carbohydrates)

    def __mul__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            return NotImplemented
        return FoodInfo(self.proteins * other, self.fats * other, self.carbohydrates * other)

    def __truediv__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            return NotImplemented
        return FoodInfo(self.proteins / other, self.fats / other, self.carbohydrates / other)

    def __floordiv__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            return NotImplemented
        return FoodInfo(self.proteins // other, self.fats // other, self.carbohydrates // other)


food1 = FoodInfo(10, 20, 30)
food2 = FoodInfo(10, 20, 30)

not_supported = [food2, [], {}, set(), '', frozenset(), ()]

for item in not_supported:
    print(food1.__add__(item))
    print(food1.__floordiv__(item))
    print(food1.__mul__(item))
    print(food1.__truediv__(item))
    