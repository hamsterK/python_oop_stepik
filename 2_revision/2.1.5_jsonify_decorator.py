"""
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""

import json
import functools


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        items = func(*args, **kwargs)
        return json.dumps(items)
    return wrapper


@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))
