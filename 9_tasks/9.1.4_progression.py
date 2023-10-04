class ArithmeticProgression:
    def __init__(self, start, step):
        self.start = start
        self.step = step

    def __next__(self):
        self.start += self.step
        return self.start - self.step

    def __iter__(self):
        return self


class GeometricProgression(ArithmeticProgression):
    def __next__(self):
        self.start *= self.step
        return self.start // self.step


progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')


print()

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')
