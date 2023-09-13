from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_obj = open(filename, mode=mode)
    except Exception as err:
        yield None, err
    else:
        try:
            yield file_obj, None
        finally:
            file_obj.close()


with open('Ellies_jokes.txt', 'w') as file:
    file.write('Знаешь, кто не прав? Лев\n')
    file.write('Что треугольник сказал кругу? Катись отсюда')

with safe_open('Ellies_jokes.txt') as file:
    file, error = file
    print(error)
    print(file.read())
