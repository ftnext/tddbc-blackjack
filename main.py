from typing import List


class Card:
    def __init__(self, suit: str, number: int) -> None:
        self.suit = suit
        self._number = number
    
    @property
    def number(self):
        return self._number if self._number < 11 else 10


def calculate_score(cards: List['Card']) -> int:
    total = 0
    for card in cards:
        total += card.number
    return total
