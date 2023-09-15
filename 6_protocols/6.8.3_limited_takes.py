class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError("Атрибут не найден")
        if self._times == 0:
            raise MaxCallsException("Превышено количество доступных обращений")
        self._times -= 1
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value


class Programmer:
    name = LimitedTakes(1)


programmer = Programmer()

try:
    print(programmer.name)
except AttributeError as e:
    print(e)
