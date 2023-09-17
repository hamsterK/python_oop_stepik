class Summator:
    def __init__(self, m=1):
        self.m = m

    def total(self, n):
        return sum(map(lambda x: x ** self.m, range(1, n + 1)))


class SquareSummator(Summator):
    def __init__(self):
        super().__init__(2)


class QubeSummator(Summator):
    def __init__(self):
        super().__init__(3)


class CustomSummator(Summator):
    def __init__(self, m):
        super().__init__(m)


summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()

print(summator1.total(3))    # 1 + 2 + 3
print(summator2.total(3))    # 1 + 4 + 9
print(summator3.total(3))    # 1 + 8 + 27
