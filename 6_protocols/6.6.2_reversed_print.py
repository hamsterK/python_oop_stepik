import sys
from contextlib import contextmanager


@contextmanager
def reversed_print():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield
    sys.stdout.write = original_write


print('Вывод вне блока with')

with reversed_print():
    print('Вывод внутри блока with')

print('Вывод вне блока with')
