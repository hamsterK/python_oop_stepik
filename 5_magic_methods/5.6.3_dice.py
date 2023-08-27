import random


class Dice:
    def __init__(self, sides):
        self.sides = sides

    def __call__(self):
        return random.randrange(1, self.sides + 1)
    #    return randint(1, self.sides)
    