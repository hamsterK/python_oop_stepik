class Numbers:
    def __init__(self):
        self.numbers_list = list()

    def add_number(self, num: int):
        self.numbers_list.append(num)

    def get_even(self):
        return [i for i in self.numbers_list if i % 2 == 0]

    def get_odd(self):
        return [i for i in self.numbers_list if i % 2]
