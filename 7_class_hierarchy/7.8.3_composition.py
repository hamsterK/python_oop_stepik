import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.suit}{self.rank}'


class Deck:
    def __init__(self):
        self.suits = ['♣', '♢', '♡', '♠']
        self.ranks = '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        if len(self.cards) != 52:
            raise ValueError('Перемешивать можно только полную колоду')
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise ValueError('Все карты разыграны')
        return self.cards.pop(len(self.cards) - 1)

    def __str__(self):
        return f'Карт в колоде: {len(self.cards)}'


deck = Deck()

print(deck)
print(deck.deal())
print(deck.deal())
print(deck.deal())
print(type(deck.deal()))
print(deck)
