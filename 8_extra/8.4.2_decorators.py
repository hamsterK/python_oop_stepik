import functools


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n
        self.calls = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n == 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self.n -= 1
            return func(*args, **kwargs)

        return wrapper


@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)
