import unittest

from class_01 import bike

class TestBike(unittest.TestCase):
    def setUp_bike(self):
        self.bike = bike.Bike()

    def test_that_bike_app_exists(self):
        exist = bike.Bike()
        self.assertTrue(exist)

    def test_that_bike_can_be_turned_on(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())

    def test_that_bike_can_be_turned_off(self):
        bk = bike.Bike()
        bk.turn_on()
        bk.turn_off()
        self.assertTrue(bk.get_status())

    # def test_that_bike_can_change_gear(self):
    #     bk = bike.Bike()
    #     bk.turn_on()
    #     bk.change_gear_one(0)
    #     bk.change_gear_one(1)
    #     self.assertTrue(bk.change_gear_one(1))

    def test_that_bike_can_accelerate_speed_by_1_on_gear_1(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        result1 = bk.get_bike_on_gear_1_by_1(1, 16)
        self.assertEqual(result1, 17)
