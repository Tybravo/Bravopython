import unittest

from class_01 import swapstringadd

class TestSwapStringAdd(unittest.TestCase):

    def test_that_swap_string_add_function_exist(self):
        exist = swapstringadd.swap_string_add("string1", "string2")
        self.assertTrue(exist,"abc xyz")

    def test_that_character_in_string_is_xyc_abz(self):
        confirm_characters = swapstringadd.swap_string_add("string1", "string2")
        self.assertTrue(confirm_characters, "xyc abz")
