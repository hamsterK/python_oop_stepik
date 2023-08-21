class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def get_fullname(self):
        return f'{self._name} {self._surname}'

    def set_fullname(self, new_fullname):
        parts = new_fullname.split()
        if len(parts) == 2:
            self._name, self._surname = parts
        else:
            raise ValueError("Fullname should consist of first name and last name")

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_surname(self):
        return self._surname

    def set_surname(self, new_surname):
        self._surname = new_surname

    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)
    fullname = property(get_fullname, set_fullname)


person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
