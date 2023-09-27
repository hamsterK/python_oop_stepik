import functools


class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        for item in args + tuple(kwargs.values()):
            if not isinstance(item, (int, float)):
                raise TypeError('Аргументы должны принадлежать типам int или float')
        return self.func(*args, **kwargs)


@takes_numbers
def mul(a, b=2):
    return a * b


try:
    print(mul(1, b='2'))
except TypeError as error:
    print(error)
