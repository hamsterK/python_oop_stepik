class UpperPrintString(str):
    def __str__(self):
        return super().__str__().upper()


s1 = UpperPrintString('beegeek')
s2 = UpperPrintString('BeeGeek')

print(s1)
print(s2)
