def limited_hash(left, right, hash_function=hash):
    def inner_hash_function(obj):
        hash_value = hash_function(obj)
        if hash_value < left:
            hash_value = right - (left - hash_value - 1) % (right - left + 1)
        elif hash_value > right:
            hash_value = left + (hash_value - right - 1) % (right - left + 1)
        return hash_value
    return inner_hash_function


hash_function = limited_hash(10, 15)

print(hash_function(16))
print(hash_function(17))
print(hash_function(21))
print(hash_function(22))
print(hash_function(23))
