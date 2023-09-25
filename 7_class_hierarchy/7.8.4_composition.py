class Queue(dict):
    def add(self, elem):
        key, value = elem
        if key in self:
            del self[key]
        self[key] = value

    def pop(self):
        if not self:
            raise KeyError('Очередь пуста')
        key, value = tuple(self.items())[0]
        del self[key]
        return key, value

    def __repr__(self):
        return f'{type(self).__name__}({list(self.items())})'


queue = Queue({'one': 1, 'two': 2})

print(len(queue))
queue.add(('three', 1))
print(len(queue))
