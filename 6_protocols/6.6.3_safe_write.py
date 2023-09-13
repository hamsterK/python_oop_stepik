from contextlib import contextmanager
import os
import shutil


@contextmanager
def safe_write(filename):
    temp_filename = 'temp_copy.txt'
    if os.path.exists(filename):
        shutil.copyfile(filename, temp_filename)
    try:
        file = open(filename, mode='w', encoding='utf-8')
        yield file
    except Exception as error:
        print(f'Во время записи в файл было возбуждено исключение {error.__class__.__name__}')
        os.remove(filename)
        if os.path.exists(temp_filename):
            os.rename(temp_filename, filename)
    else:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
        file.close()
