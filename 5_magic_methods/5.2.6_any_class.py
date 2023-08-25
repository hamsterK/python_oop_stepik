class AnyClass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f'AnyClass: {", ".join(self._attrs())}'

    def __repr__(self):
        return f'AnyClass({", ".join(self._attrs())})'

    def _attrs(self):
        return [f'{k}={repr(v)}' for (k, v) in self.__dict__.items()]


cowboy = AnyClass(name='John', surname='Marston')

print(str(cowboy))
print(repr(cowboy))
