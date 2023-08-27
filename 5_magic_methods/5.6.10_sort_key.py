class SortKey:
    """Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов.
    При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых
    представляет имя атрибута, участвующего в сортировке."""
    def __init__(self, *attributes):
        self.attributes = attributes

    def __call__(self, instance):
        return [getattr(instance, attribute) for attribute in self.attributes]


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))
