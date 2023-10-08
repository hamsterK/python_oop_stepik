class TicTacToe:
    def __init__(self):
        self.field = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.game_over = False

    def mark(self, i, j):
        if self.game_over:
            print('Игра окончена')
            return

        if self.field[i - 1][j - 1] == ' ':
            self.field[i - 1][j - 1] = self.player
            self.player = 'O' if self.player == 'X' else 'X'
        else:
            print('Недоступная клетка')

        self.check_winner()

    def check_winner(self):
        for row in self.field:
            if all(cell == 'X' for cell in row):
                self.game_over = True
                return 'X'
            elif all(cell == 'O' for cell in row):
                self.game_over = True
                return 'O'

        for col in range(3):
            if all(self.field[row][col] == 'X' for row in range(3)):
                self.game_over = True
                return 'X'
            elif all(self.field[row][col] == 'O' for row in range(3)):
                self.game_over = True
                return 'O'

        if all(self.field[i][i] == 'X' for i in range(3)) or all(self.field[i][2 - i] == 'X' for i in range(3)):
            self.game_over = True
            return 'X'
        elif all(self.field[i][i] == 'O' for i in range(3)) or all(self.field[i][2 - i] == 'O' for i in range(3)):
            self.game_over = True
            return 'O'

        if all(cell != ' ' for row in self.field for cell in row):
            self.game_over = True
            return 'Ничья'

        return None

    def winner(self):
        result = self.check_winner()
        if result:
            return result
        else:
            return None

    def show(self):
        lines = ['|'.join(row) for row in self.field]
        print('\n-----\n'.join(lines))


tictactoe = TicTacToe()

tictactoe.mark(1, 1)
tictactoe.mark(3, 1)
tictactoe.mark(1, 1)

tictactoe.mark(1, 3)
tictactoe.mark(1, 2)
tictactoe.mark(3, 3)
tictactoe.mark(2, 2)
tictactoe.mark(2, 3)

print(tictactoe.winner())
tictactoe.mark(2, 1)
tictactoe.show()
