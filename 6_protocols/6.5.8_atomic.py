from copy import copy, deepcopy


class Atomic:
    """Если все операции корректны (не приводят к возбуждению исключения), они должны быть применены к коллекции data.
    Если какая-либо операция некорректна, все ранее выполненные операции должны быть отменены, а коллекция data должна
    быть возвращена в исходное состояние."""
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy = deepcopy(self.data) if deep else copy(self.data)

    def __enter__(self):
        return self.copy

    def __exit__(self, exc_type, exc_val, traceback):
        if exc_type is None:
            self.data.clear()
            if isinstance(self.data, list):
                self.data.extend(self.copy)
            else:
                self.data.update(self.copy)
        return True


numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[1]

print(numbers)
