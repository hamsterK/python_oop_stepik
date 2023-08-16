"""
Функция должна возвращать единственное число — количество инверсий в последовательности sequence.
"""

from itertools import combinations


def inversions(sequence: list[int]) -> int:
    result = 0
    for seq in combinations(sequence, 2):
        current_item, next_item = seq
        if current_item > next_item:
            result += 1
    return result


sequence = [3, 1, 4, 2]

print(inversions(sequence))
