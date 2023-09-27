import functools


class exception_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        try:
            answer = self.func(*args, **kwargs)
        except Exception as error:
            return None, error.__class__
        return answer, None


@exception_decorator
def func(x):
    return 2 * x + 1


print(func(1))
print(func('bee'))
