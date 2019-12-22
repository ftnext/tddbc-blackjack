import unittest

import main as m


class CalculateScoreTestCase(unittest.TestCase):
    def test_sum_of_cards(self):
        cards = [m.Card('❤', 10), m.Card('♤', 11)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 20)

    def test_sum_of_cards_with_ace(self):
        cards = [m.Card('❤', 1), m.Card('♤', 11)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 21)

    def test_include_ace_twice(self):
        cards = [m.Card('❤', 1), m.Card('♤', 9), m.Card('❤', 1)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 21)


class PlayerTestCase(unittest.TestCase):
    def test_player_has_two_cards(self):
        player = m.Player()
        actual = len(player.cards)
        self.assertEqual(actual, 2)


class DeckTestCase(unittest.TestCase):
    def test(self):
        deck = m.Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_draw_cards(self):
        deck = m.Deck()
        card = deck.draw()
        self.assertEqual(len(deck.cards), 51)
