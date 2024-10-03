import unittest

from class_01 import countevenodd

class TestCountEvenOdd(unittest.TestCase):
    def test_that_count_even_ood_function_exist(self):
        exist = countevenodd.count_evenodd([2,1,5,7,8])
        self.assertTrue(exist,[2,1,5,7,8])

    def test_to_count_even_odd_numbers_in_a_list(self):
        count_num = countevenodd.count_evenodd([2,1,5,7,8])
        self.assertEqual(count_num,[2,3])
