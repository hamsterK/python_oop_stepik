class TypeChecked:
    def __init__(self, *args):
        self.args = args

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        if type(value) not in self.args:
            raise TypeError('Некорректное значение')
        obj.__dict__[self._attr] = value


class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)
