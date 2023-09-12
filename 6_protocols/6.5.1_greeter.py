class Greeter:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Приветствую, {self.name}!")
        return self

    def __exit__(self, exc_type, *args, **kwargs):
        print(f"До встречи, {self.name}!")


with Greeter('Кейв'):
    print('...')
    