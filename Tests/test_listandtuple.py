import unittest

from class_01 import listandtuple

class TestListAndTuple(unittest.TestCase):
    def test_that_list_and_tuple_function_exist(self):
        exists = listandtuple.list_tuple("34,67,55,33,12,98")
        self.assertIsNotNone(exists)
