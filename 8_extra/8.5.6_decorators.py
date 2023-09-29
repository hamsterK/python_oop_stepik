def auto_repr(args, kwargs):
    def wrapper(cls):
        def __repr__(self):
            cls_args = [repr(self.__dict__[k]) for k in args]
            cls_kwargs = [f'{k}={self.__dict__[k]!r}' for k in kwargs]
            return f'{type(self).__name__}({", ".join(cls_args + cls_kwargs)})'

        cls.__repr__ = __repr__
        return cls

    return wrapper


@auto_repr(args=['name', 'surname'], kwargs=[])
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


person = Person('Gvido', 'van Rossum')

print(person)
