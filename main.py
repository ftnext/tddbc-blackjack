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

    def __repr__(self):
        return f'{self.suit.value}{self._number}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in [Suit.HEART, Suit.SPADE, Suit.CLOVER, Suit.DIAMOND]:
            for number in range(13):
                self.cards.append(Card(suit, number + 1))
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, cards: List['Card']):
        assert len(cards) == 2
        self.cards = cards


class Dealer:
    def __init__(self, cards: List['Card']):
        assert len(cards) == 2
        self.cards = cards


class Game:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer([self.deck.draw(), self.deck.draw()])

        self.players = []
        for i in range(1):
            player = Player([self.deck.draw(), self.deck.draw()])
            self.players.append(player)

    def play(self, policy):
        while policy(self.players[0]):
            self.players[0].cards.append(self.deck.draw())
        while dealer_policy(self.dealer.cards):
            self.dealer.cards.append(self.deck.draw())

    def result(self):
        dealer_score = calculate_score(self.dealer.cards)
        result = {}
        for player in self.players:
            player_score = calculate_score(player.cards)

            if player_score > 21:
                result[player] = "Lose"
                continue

            if dealer_score > 21:
                result[player] = "Win"
                continue

            if dealer_score == player_score:
                result[player] = "Draw"
            elif dealer_score > player_score:
                result[player] = "Lose"
            else:
                result[player] = "Win"

        return result


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


def dealer_policy(cards):
    score = calculate_score(cards)
    return score <= 16


def terminal_user_policy(player):
    print("あなたの手札:", player.cards)
    user_input = input("カードを引きますか？ [Yes/no]: ").strip(" \n")
    if len(user_input) == 0:
        return True
    action = user_input[0].lower() == "y"
    return action


def main():
    game = Game()
    game.play(terminal_user_policy)

    print("ディーラーの手札:", game.dealer.cards)
    print("ディーラーのスコア", calculate_score(game.dealer.cards))
    print("あなたのスコア", calculate_score(game.players[0].cards))
    results = game.result()
    print("勝敗", results[game.players[0]])


if __name__ == '__main__':
    main()
