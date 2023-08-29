class Ord:
    def __getattribute__(self, item):
        return ord(item)


obj = Ord()

print(obj.a)
print(obj.b)
