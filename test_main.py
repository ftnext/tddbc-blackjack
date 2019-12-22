import unittest

import main as m


class CalculateScoreTestCase(unittest.TestCase):
    def test_sum_of_cards(self):
        cards = [m.Card(m.Suit.HEART, 10), m.Card(m.Suit.SPADE, 11)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 20)

    def test_sum_of_cards_with_ace(self):
        cards = [m.Card(m.Suit.HEART, 1), m.Card(m.Suit.SPADE, 11)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 21)

    def test_include_ace_twice(self):
        cards = [m.Card(m.Suit.HEART, 1), m.Card(m.Suit.SPADE, 9), m.Card(m.Suit.HEART, 1)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 21)


class PlayerTestCase(unittest.TestCase):
    def test_player_has_two_cards(self):
        deck = m.Deck()
        player = m.Player([deck.draw(), deck.draw()])
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


class DealerTestCase(unittest.TestCase):
    def test_has_two_cards(self):
        deck = m.Deck()
        dealer = m.Dealer([deck.draw(), deck.draw()])
        actual = len(dealer.cards)
        self.assertEqual(actual, 2)
    
    def test_should_return_true_when_given_16(self):
        cards = [m.Card(m.Suit.CLOVER, 10), m.Card(m.Suit.DIAMOND, 6)]
        actual = m.dealer_policy(cards)
        self.assertTrue(actual)
    
    def test_should_return_false_when_given_17(self):
        cards = [m.Card(m.Suit.CLOVER, 10), m.Card(m.Suit.DIAMOND, 7)]
        actual = m.dealer_policy(cards)
        self.assertFalse(actual)


class GameTestCase(unittest.TestCase):
    def test_play(self):
        game = m.Game()
        game.play(lambda player: len(player.cards) < 5)
        self.assertEqual(len(game.players[0].cards), 5)

    def test_result(self):
        game = m.Game()
        game.dealer.cards = [m.Card(m.Suit.CLOVER, 10), m.Card(m.Suit.DIAMOND, 7)]
        for player in game.players:
            player.cards = [m.Card(m.Suit.CLOVER, 10), m.Card(m.Suit.DIAMOND, 8)]
        actual = game.result()
        self.assertEqual(actual, { game.players[0]: "Win"})

