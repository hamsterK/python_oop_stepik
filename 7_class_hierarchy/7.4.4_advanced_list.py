class AdvancedList(list):
    def join(self, sep_custom=' '):
        return sep_custom.join(map(str, self))

    def map(self, func):
        for i in range(len(self)):
            self[i] = func(self[i])

    def filter(self, func):
        self[:] = filter(func, self)


advancedlist = AdvancedList([1, 2, 3, 4, 5])

advancedlist.map(lambda x: -x)

print(advancedlist)
