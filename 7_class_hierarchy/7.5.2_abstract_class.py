from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal_new, vertical_new):
        pass


class King(ChessPiece):
    def can_move(self, horizontal_new, vertical_new):
        horizontal_diff = abs(ord(self.horizontal) - ord(horizontal_new))
        vertical_diff = abs(self.vertical - vertical_new)
        return horizontal_diff <= 1 and vertical_diff <= 1 and (horizontal_diff + vertical_diff) > 0


class Knight(ChessPiece):
    def can_move(self, horizontal_new, vertical_new):
        horizontal_diff = abs(ord(self.horizontal) - ord(horizontal_new))
        vertical_diff = abs(self.vertical - vertical_new)
        return (horizontal_diff == 2 and vertical_diff == 1) or (horizontal_diff == 1 and vertical_diff == 2)


king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))
