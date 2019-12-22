import unittest

import main as m


class CalculateScoreTestCase(unittest.TestCase):
    def test_sum_of_numbers(self):
        scores = [10, 11]

        actual = m.calculate_score(scores)

        self.assertEqual(actual, 21)

    def test_sum_of_cards(self):
        cards = [m.Card('❤', 10), m.Card('♤', 11)]
        actual = m.calculate_score(cards)
        self.assertEqual(actual, 21)
