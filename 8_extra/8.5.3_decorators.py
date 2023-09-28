import json


def jsonattr(file_name):
    def wrapper(cls):
        with open(file_name, 'r', encoding='utf-8') as output_file:
            data = output_file.read()
            js = json.loads(data)
            for key, value in js.items():
                setattr(cls, key, value)
        return cls
    return wrapper


with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)
