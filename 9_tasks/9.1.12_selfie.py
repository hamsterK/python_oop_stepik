class Selfie:
    def __init__(self):
        self.states = []
        self.current_state = -1

    def save_state(self):
        self.states.append(self.__dict__.copy())
        self.current_state = len(self.states) - 1

    def recover_state(self, index):
        if 0 <= index < len(self.states):
            new_selfie = Selfie()
            new_selfie.__dict__.update(self.states[index])
            new_selfie.states = self.states[:index]
            return new_selfie
        else:
            return self

    def n_states(self):
        return len(self.states)


# TEST_4:
def sum_a_b(a, b):
    return a + b


def sub_a_b(a, b):
    return a - b


def mul_a_d(a, b):
    return a * b


def truediv_a_b(a, b):
    return a / b


obj = Selfie()
obj.sum_a_b = sum_a_b
print(obj.sum_a_b(1, 2))
obj.save_state()

obj.sub_a_b = sub_a_b
print(obj.sub_a_b(1, 2))
obj.save_state()

obj.mul_a_d = mul_a_d
print(obj.mul_a_d(1, 2))
obj.save_state()

obj.truediv_a_b = truediv_a_b
print(obj.truediv_a_b(1, 2))
obj.save_state()

print(obj.n_states())
obj = obj.recover_state(1)

print(obj.n_states())

# EXPECTED OUTPUT:
# 3
# -1
# 2
# 0.5
# 4
# 1
