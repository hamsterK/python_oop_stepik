"""
Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable
в исходном порядке, а затем возбуждает исключение StopIteration.

Класс LoopTracker должен иметь четыре свойства:

accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором
на данный момент

empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент
опустевшего итератора

first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор
не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение
ttributeError с текстом:
Исходный итерируемый объект пуст

last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный
момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError
с текстом:
Последнего элемента нет

Класс LoopTracker должен иметь один метод экземпляра:
is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
"""


class LoopTracker:
    def __init__(self, iterable):
        self._iterable = list(iterable)
        self._first = 0
        self._accesses = 0
        self._empty_accesses = 0
        self._last = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._iterable:
            self._accesses += 1
            self._last = self._iterable.pop(0)
            return self._last
        self._empty_accesses += 1
        raise StopIteration

    def is_empty(self):
        return not bool(self._iterable)

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._iterable:
            self._first = self._iterable[0]
            return self._first
        raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        if self._accesses:
            return self._last
        raise AttributeError('Последнего элемента нет')


loop_tracker = LoopTracker([1, 2, 3])
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)

print(next(loop_tracker))
print(loop_tracker.first)
