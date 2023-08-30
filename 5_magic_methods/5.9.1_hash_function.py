def hash_function(obj):
    temp1 = int()
    for i in range(len(str(obj)) // 2):
        temp1 += ord(str(obj)[i]) * ord(str(obj)[-1 - i])
    if len(str(obj)) % 2:
        temp1 += ord(str(obj)[len(str(obj)) // 2])

    temp2 = int()
    for i in range(0, len(str(obj)), 2):
        temp2 += ord(str(obj)[i]) * (i + 1)
    for i in range(1, len(str(obj)), 2):
        temp2 -= ord(str(obj)[i]) * (i + 1)

    return (temp1 * temp2) % 123456791
