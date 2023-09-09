class MutableString:
    def __init__(self, string=''):
        self.string = string

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()

    def __str__(self):
        return self.string

    def __repr__(self):
        return f"MutableString('{self.string}')"

    def __len__(self):
        return len(self.string)

    def __iter__(self):
        return iter(self.string)

    def __delitem__(self, key):
        self.string = list(self.string)
        del self.string[key]
        self.string = ''.join(self.string)

    def __setitem__(self, key, value):
        self.string = list(self.string)
        self.string[key] = value
        self.string = ''.join(self.string)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return MutableString(self.string[item])
        return self.string[item]

    def __add__(self, other):
        return MutableString(self.string + other.string)


mutablestring = MutableString('beegeek')

del mutablestring[2:5]
del mutablestring[1:5:2]
print(mutablestring)
