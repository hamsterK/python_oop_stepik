class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattribute__(self, name):
        if name == 'total':
            return object.__getattribute__(self, 'price') * object.__getattribute__(self, 'quantity')
        elif name == 'name':
            return object.__getattribute__(self, 'name').title()
        return object.__getattribute__(self, name)


fruit = Item('banana', 15, 5)

print(fruit.name)
print(fruit.total)
