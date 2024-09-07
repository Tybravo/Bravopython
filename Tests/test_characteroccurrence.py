import unittest
from class_01 import characterccurrence


class TestWordOccurrence(unittest.TestCase):
    def test_chara_occurrence_exist(self):
        value = characterccurrence.character_occurrence("adetayo")
        self.assertEqual({'a':2, 'd':1,'e':1, 't':1, 'y':1, 'o':1}, value)

    def test_chara_occurrence_not_exist(self):
        empty_word = characterccurrence.character_occurrence("")
        self.assertEqual({}, empty_word)

    def test_chara_occurrence_ignore_case(self):
        ignore_case = characterccurrence.character_occurrence("MaxiMum")
        self.assertEqual({'M':2, 'a':1,'x':1, 'i':1, 'u':1, 'm':1}, ignore_case)

    def test_chara_occurrence_contain_digit_alphabet(self):
        alphabets = characterccurrence.character_occurrence("Ade4438888")
        self.assertEqual({'A':1, 'd':1,'e':1, '4':2, '3':1, '8':4}, alphabets)

