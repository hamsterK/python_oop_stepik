class Counter:
    def __init__(self, start=0):
        self.value = start

    def inc(self, n=1):
        self.value += n

    def dec(self, n=1):
        self.value = max(self.value - n, 0)


class DoubledCounter(Counter):
    def inc(self, num=1):
        self.value += num * 2

    def dec(self, num=1):
        if num * 2 - self.value > 0:
            self.value = 0
        else:
            self.value -= num * 2


counter = DoubledCounter(20)

print(counter.value)
counter.inc()
counter.inc(5)
print(counter.value)
counter.dec()
counter.dec(10)
print(counter.value)
counter.dec(10)
print(counter.value)
