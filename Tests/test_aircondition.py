import unittest
from class_01 import airconditioner

class TestAirconditioner(unittest.TestCase):
    def test_if_air_condition_is_on(self, isOn=1):
        result = airconditioner.aircon(isOn)
        self.assertEqual(result, 1)
        