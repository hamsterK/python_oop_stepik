class User:
    def __init__(self, name='', age=''):
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError('Некорректное имя')
        else:
            self._name = name
        if not isinstance(age, int) or age not in range(0, 111):
            raise ValueError('Некорректный возраст')
        else:
            self._age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str) or not new_name.isalpha():
            raise ValueError('Некорректное имя')
        else:
            self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if not isinstance(new_age, int) or new_age not in range(0, 111):
            raise ValueError('Некорректный возраст')
        else:
            self._age = new_age


user = User('Меган', 37)

invalid_names = (-1, True, '', [], '123456', 'Меган906090')

for name in invalid_names:
    try:
        user.set_name(name)
    except ValueError as e:
        print(e)
