import functools


class ignore_exception:
    def __init__(self, *args):
        self.exceptions = args

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                answer = func(*args, **kwargs)
            except Exception as error:
                if type(error) in self.exceptions:
                    print(f'Исключение {error.__class__.__name__} обработано')
                else:
                    raise error
            else:
                return answer
        return wrapper


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x


func(0)
