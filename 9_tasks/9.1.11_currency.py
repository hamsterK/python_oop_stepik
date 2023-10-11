class Currency:
    __RATE = {
        'EUR': {'EUR': 1, 'USD': 1.1, 'RUB': 90},
        'USD': {'EUR': 1 / 1.1, 'USD': 1, 'RUB': 1 / 1.1 * 90},
        'RUB': {'EUR': 1 / 90, 'USD': 1 / 90 * 1.1, 'RUB': 1}
    }

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

    def change_to(self, new_currency):
        self.value *= self.__RATE[self.currency][new_currency]
        self.currency = new_currency

    def __str__(self):
        return f'{round(self.value, 2)} {self.currency}'

    def __add__(self, other):
        other.change_to(self.currency)
        return Currency(self.value + other.value, self.currency)

    def __sub__(self, other):
        other.change_to(self.currency)
        return Currency(self.value - other.value, self.currency)

    def __mul__(self, other):
        other.change_to(self.currency)
        return Currency(self.value * other.value, self.currency)

    def __truediv__(self, other):
        other.change_to(self.currency)
        return Currency(self.value / other.value, self.currency)


print(Currency(5, 'EUR') + Currency(5, 'EUR'))
print(Currency(11, 'USD') - Currency(5, 'EUR'))
print(Currency(5, 'RUB') * Currency(11, 'USD'))
print(Currency(5, 'USD') / Currency(5, 'EUR'))
