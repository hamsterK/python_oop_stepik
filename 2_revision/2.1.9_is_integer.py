import re


def is_integer(number):
    return re.fullmatch(r'-?\d+', number) is not None


print(is_integer('5f'))
