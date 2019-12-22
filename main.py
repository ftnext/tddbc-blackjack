from typing import List


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ['♥','♠','♣','◆']:
            for number in range(13):
                self.cards.append(Card(suit, number))




class Player:
    def __init__(self):
        self.cards = [Card('❤', 1), Card('♤', 11)]


class Card:
    def __init__(self, suit: str, number: int) -> None:
        self.suit = suit
        self._number = number

    @property
    def number(self):
        return self._number if self._number < 11 else 10

    @property
    def is_ace(self):
        return self._number == 1


def calculate_score(cards: List['Card']) -> int:
    total = 0
    contain_ace = 0
    for card in cards:
        if card.is_ace:
            contain_ace += 1
        total += card.number

    for i in range(contain_ace):
        if total <= 11:
            total += 10

    return total
