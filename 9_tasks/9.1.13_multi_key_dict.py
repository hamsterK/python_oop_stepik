from collections import UserDict


class MultiKeyDict(UserDict):
    def __init__(self, *args, **kwargs):
        self._aliases = {}
        super().__init__(*args, **kwargs)

    def alias(self, key, alias):
        self._aliases[alias] = key

    def __getitem__(self, key):
        return self.data.get(key) or self.data.get(self._aliases[key])

    def __setitem__(self, key, value):
        if key in self.data or key not in self._aliases:
            self.data[key] = value
        else:
            self.data[self._aliases[key]] = value

    def __delitem__(self, del_key):
        for alias_key, key in self._aliases.items():
            if key == del_key:
                self.data[alias_key] = self.data[del_key]
        del self.data[del_key]


# TEST_1:
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
print(multikeydict['z'])
multikeydict['t'] += 1
print(multikeydict['x'])

multikeydict.alias('y', 'z')
multikeydict['z'] += [30]
print(multikeydict['y'])

# TEST_2:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])

try:
    print(multikeydict['x'])
except KeyError:
    print('Ключ отсутствует')

# TEST_3:
multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])

# multikeydict['y'] += [30]
print(multikeydict['y'])

# TEST_4:
multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])

# TEST_5:
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['x'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

# TEST_6:
mkey = MultiKeyDict(x=1)
mkey.alias('x', 'y')
mkey.alias('x', 'z')
print(mkey['x'], mkey['y'], mkey['z'])
mkey['y'] += 1
print(mkey['x'], mkey['y'], mkey['z'])

# TEST_7:
multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])
print(multikeydict1['y'])
print(multikeydict2['z'])

multikeydict1['a'] = 4
print(multikeydict1['a'])

# TEST_8:
multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
multikeydict.alias('x', 't')
del multikeydict['x']
multikeydict['z'] += 1
print(multikeydict['z'])
print(multikeydict['t'])
