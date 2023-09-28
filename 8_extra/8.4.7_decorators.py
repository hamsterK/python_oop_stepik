import functools


class type_check:
    def __init__(self, *args):
        self.types = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args):
            for i in range(len(args)):
                if i <= len(self.types):
                    if type(args[i]) != type(self.types[i]):
                        raise TypeError
            return func(*args)
        return wrapper


@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))
