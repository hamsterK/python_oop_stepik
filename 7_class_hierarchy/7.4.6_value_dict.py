class ValueDict(dict):
    def key_of(self, value_to_search):
        for key, value in self.items():
            if value == value_to_search:
                return key
        return None

    def keys_of(self, value_to_search):
        items = list()
        for key, value in self.items():
            if value == value_to_search:
                items.append(key)
        return items


valuedict = ValueDict({'apple': 1, 'banana': 2, 'orange': 2})

print(valuedict.key_of(2))
print(*valuedict.keys_of(2))
