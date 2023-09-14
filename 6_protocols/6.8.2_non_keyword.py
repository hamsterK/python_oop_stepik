from keyword import kwlist


class NonKeyword:
    def __init__(self, name):
        self._attr = name

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        obj.__dict__[self._attr] = value


class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)
