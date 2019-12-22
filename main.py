from typing import List


class Card:
    def __init__(self, suit: str, number: int) -> None:
        pass


def calculate_score(scores: List['Card']) -> int:
    return sum(scores)
