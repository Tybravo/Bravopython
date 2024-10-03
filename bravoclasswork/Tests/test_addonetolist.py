import unittest

from class_01 import addonetolist

class TestAddOneToList(unittest.TestCase):
    def test_add_one_tolist_Func_not_empty(self):
        avail = addonetolist.add_one([1])
        self.assertIsNotNone(avail, [1])

    def test_add_one_tolist_and_split(self):
        value = addonetolist.add_one([9,9,9])
        self.assertEqual(value, [1,0,0,0])

