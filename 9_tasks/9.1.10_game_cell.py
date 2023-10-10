from random import choice as r_ch


class Cell:
    def __init__(self, col, row, mine=False):
        self.col = col
        self.row = row
        self.mine = mine
        self.open = False
        self.neighbours = 0


class Game:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[Cell(i, j) for i in range(cols)] for j in range(rows)]
        self.mines_counter = 0
        while self.mines_counter < self.mines:
            row = r_ch(range(self.rows))
            col = r_ch(range(self.cols))
            if not self.board[row][col].mine:
                self.board[row][col].mine = True
                self.mines_counter += 1
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.board[row][col]
                cell.neighbours = self.get_neighbours_count(row, col)

    def get_neighbours_count(self, row, col):
        count = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if 0 <= row + i < self.rows and 0 <= col + j < self.cols:
                    count += self.board[row + i][col + j].mine
        return count


game = Game(14, 18, 40)
print(game.rows)

cell = game.board[0][0]

print(cell.row)            # 0; строка ячейки
print(cell.col)            # 0; столбец ячейки
print(cell.mine)           # True или False в зависимости от того, содержит ячейка мину или нет
print(cell.open)           # True или False в зависимости от того, открыта ячейка или нет, по умолчанию закрыта
print(cell.neighbours)     # число от 0 до 8, количество мин в соседних ячейках