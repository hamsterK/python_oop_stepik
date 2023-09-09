from collections import UserDict, defaultdict


class Grouper(UserDict):
    def __init__(self, iterable, key):
        self.key = key
        self.data = defaultdict(list)
        for i in iterable:
            self.data[key(i)].append(i)

    def __iter__(self):
        yield from self.data.items()

    def add(self, obj):
        self.data[self.key(obj)].append(obj)

    def group_for(self, obj):
        return self.key(obj)


grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)

print(grouper[2])
print(grouper[3])
print(grouper[4])
