import functools


class returns:
    def __init__(self, datatype):
        self.datatype = datatype

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if len(args + tuple(kwargs.values())) == 0:
                raise TypeError
            for item in args:
                if not isinstance(item, self.datatype):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper


@returns(list)
def append_this(li, elem):
    '''append_this docs'''
    return li + [elem]

print(append_this.__name__)
print(append_this.__doc__)
print(append_this([1, 2, 3], elem=4))
