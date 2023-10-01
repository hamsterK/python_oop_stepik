import string


class CaesarCipher:
    def __init__(self, n):
        self.n = n

    def encode(self, txt):
        return ''.join((self.magic(i, self.n) if i in string.ascii_letters else i for i in txt))

    def decode(self, txt):
        return ''.join((self.magic(i, -self.n) if i in string.ascii_letters else i for i in txt))

    def magic(self, symb, n):
        if symb in string.ascii_lowercase:
            if (x := (ord(symb) + n)) > 122 or x < 97:
                return (chr(x - 26), chr(x + 26))[x < 97]
            return chr(x)
        else:
            if (x := (ord(symb) + n)) > 90 or x < 65:
                return (chr(x - 26), chr(x + 26))[x < 65]
            return chr(x)


cipher = CaesarCipher(10)

print(cipher.encode('Beegeek'))
print(cipher.decode('Gjjljjp'))