class FuzzyString(str):
    def __eq__(self, other):
        try:
            return str.lower(self) == str.lower(other)
        except TypeError:
            return NotImplemented

    def __ne__(self, other):
        try:
            return str.lower(self) != str.lower(other)
        except TypeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return str.lower(self) < str.lower(other)
        except TypeError:
            return NotImplemented

    def __gt__(self, other):
        try:
            return str.lower(self) > str.lower(other)
        except TypeError:
            return NotImplemented

    def __le__(self, other):
        try:
            return str.lower(self) <= str.lower(other)
        except TypeError:
            return NotImplemented

    def __ge__(self, other):
        try:
            return str.lower(self) >= str.lower(other)
        except TypeError:
            return NotImplemented

    def __contains__(self, item):
        try:
            return str.lower(item) in str.lower(self)
        except TypeError:
            return NotImplemented
