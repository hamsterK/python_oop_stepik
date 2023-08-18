from collections import namedtuple
from collections import Counter


class Postman:
    def __init__(self):
        self.delivery_data = list()
        self.Address = namedtuple('Address', ['street', 'house_number', 'apartment'])

    def add_delivery(self, street, house_number, apartment):
        self.delivery_data.append(self.Address(street, house_number, apartment))

    def get_houses_for_street(self, street):
        return list(Counter([address.house_number for address in self.delivery_data if address.street == street]))

    def get_flats_for_house(self, street, house_number):
        return list(Counter([address.apartment for address in self.delivery_data if address.street == street
                and address.house_number == house_number]))


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
