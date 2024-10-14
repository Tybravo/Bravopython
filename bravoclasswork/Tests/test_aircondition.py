import unittest

from class_01 import aircondition

class TestAirCondition(unittest.TestCase):
    def setUp(self):
        self.ac = aircondition.AirCondition()

    def test_that_ac_app_exist(self):
        exist = aircondition.AirCondition()
        self.assertTrue(exist)

    def test_that_ac_can_be_turned_on(self):
        ac = aircondition.AirCondition()
        ac.turn_off()
        ac.turn_on()
        self.assertTrue(ac.get_bike_status())

    def test_that_ac_can_be_turned_off(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        ac.turn_off()
        self.assertFalse(ac.get_bike_status())

    def test_that_temperature_starts_from_16_when_turned_on(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        start_16 = ac.get_temp_start_from_16(16)
        self.assertEqual(start_16, 16)

    def test_that_temperature_can_be_increased(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        ac.get_temp_increased(16)
        ac.get_temp_increased(17)
        increase = ac.get_temp_increased(18)
        self.assertEqual(increase, 19)

    def test_that_temperature_can_be_decreased(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        increase = ac.get_temp_increased(16)
        self.assertEqual(increase, 17)
        decrease = ac.get_temp_decreased(17)
        self.assertEqual(decrease, 16)

    def test_that_temperature_cannot_go_beyond_30(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        increase = ac.get_temp_maintain_30(30)
        self.assertEqual(increase, 30)

    def test_that_temperature_cannot_go_below_16(self):
        ac = aircondition.AirCondition()
        ac.turn_on()
        decrease = ac.get_temp_maintain_16(16)
        self.assertEqual(decrease, 16)





