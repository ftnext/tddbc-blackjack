from typing import List


class Card:
    def __init__(self, suit: str, number: int) -> None:
        self.suit = suit
        self.number = number


def calculate_score(cards: List['Card']) -> int:
    total = 0
    for card in cards:
        total += card.number
    return total
