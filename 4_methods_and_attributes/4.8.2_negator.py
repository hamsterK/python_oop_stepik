from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def neg_num(data):
        return data * -1

    @neg.register(bool)
    @staticmethod
    def neg_bool(data):
        return not data


print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))
