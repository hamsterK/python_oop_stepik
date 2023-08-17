import re


def is_decimal(number):
    return bool(re.fullmatch(r'-?\d*\.?\d*', number) and re.search('\d', number))


print(is_decimal('.10'))
