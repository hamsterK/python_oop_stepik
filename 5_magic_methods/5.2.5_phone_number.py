class PhoneNumber:
    def __init__(self, phone_number):
        self.phone_number = ''.join(phone_number.split())

    def __str__(self):
        return f"({self.phone_number[:3]}) {self.phone_number[3:6]}-{self.phone_number[6:]}"

    def __repr__(self):
        return f"PhoneNumber('{self.phone_number}')"


phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))
