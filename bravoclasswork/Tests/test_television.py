import unittest

from class_01 import television

class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.television = television.Television()

    def test_that_television_exists(self):
        exist = television.Television()
        self.assertTrue(exist)

    def test_that_television_can_be_turned_on(self):
        tv = television.Television()
        tv._turn_on()
        self.assertTrue(tv.get_is_on())

    def test_that_television_can_be_turned_off(self):
        tv = television.Television()
        tv._turn_on()
        tv._turn_off()
        self.assertFalse(tv.get_is_on())

    def test_that_television_can_get_volume_when_turned_on(self):
        tv = television.Television()
        tv._turn_on()
        self.assertTrue(tv.get_is_on())
        self.assertTrue(tv.get_volume())

    def test_that_television_cannot_get_volume_when_turned_off(self):
        tv = television.Television()
        tv._turn_on()
        tv._turn_off()
        self.assertFalse(tv.get_volume())

    def test_that_volume_can_be_increased(self):
        tv = television.Television()
        tv._turn_on()
        tv.set_volume(2)
        tv.increase_volume()
        tv.increase_volume()
        self.assertEqual(tv.get_volume(),4)

    def test_that_volume_can_be_decreased(self):
        tv = television.Television()
        tv._turn_on()
        tv.set_volume(6)
        tv.decrease_volume()
        tv.decrease_volume()
        self.assertEqual(tv.get_volume(),4)

    def test_that_volume_cannot_be_lower_than_zero(self):
        tv = television.Television()
        tv._turn_on()
        tv.set_volume(1)
        tv.decrease_volume()
        tv.decrease_volume()
        self.assertFalse(tv.get_volume(), -1)

    def test_that_volume_cannot_be_higher_than_10(self):
        tv = television.Television()
        tv._turn_on()
        tv.set_volume(7)
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        tv.increase_volume()
        self.assertFalse(tv.get_volume(),11)

    def test_that_television_can_get_channel_when_turned_on(self):
        tv = television.Television()
        tv._turn_on()
        self.assertTrue(tv.get_is_on())
        self.assertTrue(tv.get_channel())

    def test_that_television_cannot_get_channel_when_turned_off(self):
        tv = television.Television()
        tv._turn_on()
        tv._turn_off()
        self.assertFalse(tv.get_channel())

    def test_that_television_can_change_channel_up_when_turned_on(self):
        tv = television.Television()
        tv._turn_on()
        tv.set_channel(1)
        tv.channel_up()
        tv.channel_up()
        self.assertEqual(tv.get_channel(), 3)





