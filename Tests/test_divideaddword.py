import unittest
from class_01 import divideaddword

class TestDivideAddWord(unittest.TestCase):
    def test_divide_add_word_function_exist(self):
        exist = divideaddword.divide_add_word("helloo")
        self.assertTrue(exist, "helloo")

    def test_divide_add_word_ce_at_the_middle_for_divisible_word(self):
        new_word = divideaddword.divide_add_word("helloo")
        self.assertEqual(new_word,"helceloo")

    def test_cannot_divide_add_word_at_the_end(self):
        end_word = divideaddword.divide_add_word("joy")
        self.assertEqual(end_word,"joyce" )

    def test_cannot_add_ce_to_middle_for_indivisible_word(self):
        new_word2 = divideaddword.divide_add_word("adetayo")
        self.assertTrue(new_word2,"adetayoce")

    def test_cannot_add_ce_to_the_end_of_divisible_word(self):
        end_word2 = divideaddword.divide_add_word("mike")
        self.assertTrue(end_word2,"miceke")
