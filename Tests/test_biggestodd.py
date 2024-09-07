import unittest
from class_01 import biggestodd


class TestBiggestOdd(unittest.TestCase):

    def test_that_biggest_odds_function_exist(self):
        biggestodd.biggest_odd("23956")

    def test_biggest_function_returns_biggest_odds(self):
        result = biggestodd.biggest_odd("23956")
        self.assertEqual(result, 9)

