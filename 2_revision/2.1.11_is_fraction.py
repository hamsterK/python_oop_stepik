import re


def is_fraction(number):
    return bool(re.fullmatch(r'-?\d+/\d*[1-9]\d*', number))


print(is_fraction('1000/00004123'))
print(is_fraction('1000/0000'))
print(is_fraction('1000/00000008000'))
