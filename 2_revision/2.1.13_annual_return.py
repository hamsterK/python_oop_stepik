"""
Функция должна возвращать итератор, моделирующий банковский вклад. Возвращаемыми значениями итератора должны являться
размеры вклада после очередного начисления процентов percent.
"""


def annual_return(start, percent, years):
    for year in range(years):
        start = start * (100 + percent) / 100
        yield start


for value in annual_return(70000, 8, 10):
    print(round(value))
