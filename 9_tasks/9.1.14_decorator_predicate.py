class predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) and other(*args, **kwargs))

    def __or__(self, other):
        return predicate(lambda *args, **kwargs: self(*args, **kwargs) or other(*args, **kwargs))

    def __invert__(self):
        return predicate(lambda *args, **kwargs: not self(*args, **kwargs))


# TEST_1:
@predicate
def to_be():
    return True


print((to_be | ~to_be)())                     # True; равнозначно to_be() or not to_be()


@predicate
def is_equal(a, b):
    return a == b


@predicate
def is_less_than(a, b):
    return a < b


print((is_less_than | is_equal)(1, 2))        # True; равнозначно is_less_than(1, 2) or is_equal(1, 2)

print((is_less_than | is_equal)(2, b=2))      # True; равнозначно is_less_than(2, b=2) or is_equal(2, b=2)
print((is_less_than | is_equal)(a=3, b=2))    # False; равнозначно is_less_than(a=3, b=2) or is_equal(a=3, b=2)
