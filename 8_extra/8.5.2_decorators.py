"""
Словарь атрибутов класса, в отличие от словаря атрибутов экземпляра класса, является объектом типа mappingproxy,
а не dict. ип mappingproxy представляет собой упрощенный словарь. От типа dict он отличается меньшим количеством
методов, а главное — отсутствием магического метода __setitem__(). Это значит, в объект типа mappingproxy нельзя
напрямую добавить новую пару ключ-значение, а также изменить значение имеющегося ключа. Для добавления классу
необходимого атрибута можно использовать функцию setattr().
"""


def add_attr_to_class(**attrs):
    def wrapper(cls):
        for attr, value in attrs.items():
            setattr(cls, attr, value)

        return cls

    return wrapper


@add_attr_to_class(first_attr=1, second_attr=2)
class MyClass:
    pass

print(MyClass.first_attr)
print(MyClass.second_attr)
