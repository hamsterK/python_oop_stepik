class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            rounded_num = (num + 1) // 2 * 2
        else:
            rounded_num = (num // 2) * 2 + 1
        return super(RoundedInt, cls).__new__(cls, rounded_num)


print(RoundedInt(7))
print(RoundedInt(8))
print(RoundedInt(7, False))
print(RoundedInt(8, False))
