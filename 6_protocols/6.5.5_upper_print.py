import sys


class UpperPrint:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.upper_write
        return self

    def upper_write(self, text):
        self.original_write(text.upper())

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_write


print('Если жизнь одаривает вас лимонами — не делайте лимонад')
print('Заставьте жизнь забрать их обратно!')

with UpperPrint():
    print('Мне не нужны твои проклятые лимоны!')
    print('Что мне с ними делать?')

print('Требуйте встречи с менеджером, отвечающим за жизнь!')
