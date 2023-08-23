from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register(int)
    @staticmethod
    def format_int(data):
        print(f'Целое число: {data}')

    @format.register(float)
    @staticmethod
    def format_float(data):
        print(f'Вещественное число: {data}')

    @format.register(tuple)
    @staticmethod
    def format_tuple(data):
        formatted_elements = ', '.join(map(str, data))
        print(f'Элементы кортежа: {formatted_elements}')

    @format.register(list)
    @staticmethod
    def format_list(data):
        formatted_elements = ', '.join(map(str, data))
        print(f'Элементы списка: {formatted_elements}')

    @format.register(dict)
    @staticmethod
    def format_dict(data):
        # By using the repr() function, the code can recreate the object
        items = [(key, value) for key, value in data.items()]
        formatted_items = ', '.join([f'({repr(key)}, {repr(value)})' for key, value in items])
        print(f'Пары словаря: {formatted_items}')


Formatter.format([10, 20, 30, 40, 50])
Formatter.format(([1, 3], [2, 4, 6]))
Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
