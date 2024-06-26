"""
Будем считать, что игровое поле для игры в дартс представляет собой квадратную матрицу, заполненную натуральными
числами, расположенными в порядке возрастания от краев к центру. Стороной игрового поля будем называть сторону
квадратной матрицы, которую представляет это поле.

Напишите программу, которая создает поле для игры в дартс определенного размера.
"""

num = int(input())

field = [[1 for i in range(num)] for j in range(num)]
for i in range(1, num // 2 + 1):
    for j in range(i, num - i):
        for k in range(i, num - i):
            field[j][k] += 1
[print(*i) for i in field]