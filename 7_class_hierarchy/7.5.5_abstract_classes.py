from collections.abc import *


class CustomRange(Sequence):
    def __init__(self, *args):
        self.num_list = list()
        for i in args:
            if type(i) == int:
                self.num_list.append(i)
            else:
                a, b = [int(j) for j in i.split('-')]
                self.num_list.extend(range(a, b + 1))

    def __getitem__(self, item):
        return self.num_list[item]

    def __len__(self):
        return len(self.num_list)


customrange = CustomRange(1, '2-5', 5, '6-8')

print(customrange[0])
print(customrange[1])
print(customrange[2])
print(customrange[-1])
print(customrange[-2])
print(customrange[-3])
