import unittest

import main as m


class CalculateScoreTestCase(unittest.TestCase):
    def test(self):
        scores = [10, 11]

        actual = m.calculate_score(scores)

        self.assertEqual(actual, 21)
