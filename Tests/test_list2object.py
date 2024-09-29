import unittest

from class_01 import list2object

class TestList2Object(unittest.TestCase):

    def test_list2object_function_exist(self):
        exist = list2object.list2_object([1,1,2,3,2])
        self.assertIsNotNone(exist)

    def test_that_list_converted_to_object(self):
        value = list2object.list2_object([1,1,2,3,2])
        self.assertIsInstance(value, dict)

    def test_that_list_cannot_be_empty(self):
        empty_list = list2object.list2_object([])
        self.assertEqual({}, empty_list)