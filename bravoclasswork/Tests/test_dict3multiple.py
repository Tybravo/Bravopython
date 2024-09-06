import unittest
from class_01 import dict3multiples


class TestKeyCube(unittest.TestCase):
    def test_that_key_cube_function_exist(self):
        dict3multiples.list_to_dict_pow([1, 2, 3, 4, 5])


def test_that_key_cube_function_returns_dict(self):
    actual = dict3multiples.list_to_dict_pow([1, 2, 3, 4, 5])
    expected = {1:1, 2:8, 3:27, 4:64, 5:125}
    self.assertEqual(actual, expected)
