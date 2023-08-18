class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'

    def can_move(self, new_horizontal, new_vertical):
        dx = abs(ord(new_horizontal) - ord(self.horizontal))
        dy = abs(new_vertical - self.vertical)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)

    def move_to(self, new_horizontal, new_vertical):
        if self.can_move(new_horizontal, new_vertical):
            self.horizontal, self.vertical = new_horizontal, new_vertical

    def draw_board(self):
        for i in range(8, 0, -1):
            for j in range(1, 9):
                if i == self.vertical and j == ord(self.horizontal) - ord('a') + 1:
                    print(self.get_char(), end='')
                elif self.can_move(chr(ord('a') + j - 1), i):
                    print('*', end='')
                else:
                    print('.', end='')
            print()


knight = Knight('c', 3, 'white')

knight.draw_board()
