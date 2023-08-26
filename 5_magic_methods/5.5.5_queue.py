class Queue:
    def __init__(self, *args):
        self.elements = list(args)

    def __str__(self):
        return ' -> '.join(map(str, self.elements))

    def __eq__(self, other):
        return self.elements == other.elements

    def __ne__(self, other):
        return self.elements != other.elements

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*self.elements, *other.elements)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.elements.extend(other.elements)
            return self
        return NotImplemented

    def __rshift__(self, n):
        if isinstance(n, int):
            return Queue(*self.elements[n:])
        return NotImplemented

    def add(self, *args):
        self.elements.extend(args)

    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop(0)


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)
