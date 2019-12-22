import enum
import random
from typing import List


class Suit(enum.Enum):
    HEART = '♥'
    SPADE = '♠'
    CLOVER = '♣'
    DIAMOND = '◆'


class Card:
    def __init__(self, suit: Suit, number: int) -> None:
        self.suit = suit
        self._number = number

    @property
    def number(self):
        return self._number if self._number < 11 else 10

    @property
    def is_ace(self):
        return self._number == 1


class Deck:
    def __init__(self):
        self.cards = []
        for suit in [Suit.HEART, Suit.SPADE, Suit.CLOVER, Suit.DIAMOND]:
            for number in range(13):
                self.cards.append(Card(suit, number))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


deck = Deck()


class Player:
    def __init__(self):
        self.cards = [deck.draw(), deck.draw()]

    def hit(self):
        card = deck.draw()
        self.cards.append(card)


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
