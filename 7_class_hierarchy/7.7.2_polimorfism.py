class MinStat:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = []
        else:
            self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    def result(self):
        if len(self.iterable) == 0:
            return None
        return min(self.iterable)

    def clear(self):
        self.iterable = []


class MaxStat(MinStat):
    def result(self):
        if len(self.iterable) == 0:
            return None
        return max(self.iterable)


class AverageStat(MinStat):
    def result(self):
        if len(self.iterable) == 0:
            return None
        return sum(self.iterable) / len(self.iterable)


minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
