import random


class RandomLooper:
    def __init__(self, *args):
        self.elems = list()
        for arg in args:
            self.elems.extend(arg)
        random.shuffle(self.elems)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.elems):
            elem = self.elems[self.index]
            self.index += 1
            return elem
        else:
            raise StopIteration


colors = ['red', 'blue', 'green', 'purple']
shapes = ['square', 'circle', 'triangle', 'octagon']
randomlooper = RandomLooper(colors, shapes)

print(list(randomlooper))
