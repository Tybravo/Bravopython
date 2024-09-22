import unittest
from class_01 import removespecialchar

class TestRemoveSpecialChar(unittest.TestCase):
    def test_that_function_exist(self):
        exist = removespecialchar.remove_special_char("he.ll,o")
        self.assertTrue(exist, "he.ll,o")

    def test_to_remove_special_character(self):
        removal = removespecialchar.remove_special_char("he.ll,o")
        self.assertTrue(removal, "hello")
