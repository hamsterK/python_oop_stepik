class Suppress:
    def __init__(self, *exceptions):
        self.exceptions = exceptions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.exceptions:
            self.exception = exc_val
            return True
        self.exception = None
        return False


with Suppress(NameError):
    print('Этой переменной не существует -->', variable)

print('Завершение программы')
