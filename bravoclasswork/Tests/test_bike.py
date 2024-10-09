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
        self.assertFalse(bk.get_status())

    def test_that_bike_can_accelerate_speed_by_1_on_gear_1(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_accelerate1 = bk.get_bike_on_gear_accel_1_by_1(1, 15)
        self.assertEqual(auto_accelerate1, 16)

    def test_that_bike_can_accelerate_speed_by_2_on_gear_1(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_accelerate2 = bk.get_bike_on_gear_accel_2_by_2(2, 24)
        self.assertEqual(auto_accelerate2, 26)

    def test_that_bike_can_accelerate_speed_by_3_on_gear_3(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_accelerate3 = bk.get_bike_on_gear_accel_3_by_3(3, 35)
        self.assertEqual(auto_accelerate3, 38)

    def test_that_bike_can_accelerate_speed_by_4_on_gear_4(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_accelerate4 = bk.get_bike_on_gear_accel_4_by_4(4, 44)
        self.assertEqual(auto_accelerate4, 48)

    def test_that_bike_can_decelerate_speed_by_1_on_gear_1(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_decelerate1 = bk.get_bike_on_gear_decel_1_by_1(1, 15)
        self.assertEqual(auto_decelerate1, 14)

    def test_that_bike_can_decelerate_speed_by_2_on_gear_2(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_decelerate2 = bk.get_bike_on_gear_decel_2_by_2(2, 24)
        self.assertEqual(auto_decelerate2, 22)

    def test_that_bike_can_decelerate_speed_by_3_on_gear_3(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_decelerate3 = bk.get_bike_on_gear_decel_3_by_3(3, 35)
        self.assertEqual(auto_decelerate3, 32)

    def test_that_bike_can_decelerate_speed_by_4_on_gear_4(self):
        bk = bike.Bike()
        bk.turn_on()
        self.assertTrue(bk.get_status())
        auto_decelerate4 = bk.get_bike_on_gear_decel_4_by_4(4, 44)
        self.assertEqual(auto_decelerate4, 40)
