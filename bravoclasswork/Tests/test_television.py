import unittest

from class_01 import television

class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.television = television.Television()

    def test_that_television_exists(self):
        exist = television.Television()
        self.assertTrue(exist)

    def test_that_television_can_be_turned_on(self):
        is_on = television.Television()
        self.television = television.Television()
        self.assertTrue(is_on.get_is_on())

    def test_that_television_can_be_turned_off(self):
        is_on = television.Television()
        self.assertTrue(is_on.get_is_on())
        is_off = television.Television()
        self.assertTrue(is_off.get_is_on())

    def test_that_television_can_get_volume_when_turned_on(self):
        is_on = television.Television()
        self.assertTrue(is_on.get_is_on())
        self.assertTrue(is_on.get_volume())

    def test_that_television_cannot_get_volume_when_turned_off(self):
        is_on = television.Television()
        self.assertTrue(is_on.get_is_on())
        is_off = television.Television()
        self.assertTrue(is_off.get_is_on())
        self.assertTrue(is_off.get_volume())

    def test_that_volume_can_be_increased(self):
        self.television.get_is_on()
        self.television.set_volume(2)
        self.television.increase_volume()
        self.television.increase_volume()
        self.assertEqual(self.television.get_volume(),4)
