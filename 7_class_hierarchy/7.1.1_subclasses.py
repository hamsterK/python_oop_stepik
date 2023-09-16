class Counter:
    def __init__(self, start=0):
        self.start = start
        self.value = self.start

    def inc(self, num=1):
        self.value += num

    def dec(self, num=1):
        if num - self.value > 0:
            self.value = 0
        else:
            self.value -= num


class NonDecCounter(Counter):
    def dec(self, num=1):
        pass


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=10):
        self.start = start
        self.value = self.start
        self.limit = limit

    def inc(self, num=1):
        if self.value + num > self.limit:
            self.value = self.limit
        else:
            self.value += num


counter = LimitedCounter(limit=20)

print(counter.value)
counter.inc()
counter.inc(4)
print(counter.value)
counter.dec()
counter.dec(2)
print(counter.value)
counter.inc(20)
print(counter.value)
