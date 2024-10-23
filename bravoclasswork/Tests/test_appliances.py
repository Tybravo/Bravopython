import unittest
from os.path import exists

from class_01 import appliances
from class_01.appliances import LightBulb, ElectricFan, Toaster, Cooker, Blender, Speaker, NaturalGas


class TestLightBulb(unittest.TestCase):

    def test_bulb_appliance_not_empty(self):
        not_empty = self.light_bulb = LightBulb
        self.assertTrue(not_empty, True)

    def test_bub_energy_conversion(self):
        bulb = LightBulb()
        self.assertEqual(bulb.convert_energy(), "Electrical energy is converted into heat and light energy")


class TestElectricalFan(unittest.TestCase):
    def test_fan_appliance_not_empty(self):
        not_empty = self.fan = ElectricFan
        self.assertTrue(not_empty, True)

    def test_fan_energy_conversion(self):
        fan = ElectricFan()
        self.assertEqual(fan.convert_energy(), "Electrical energy is converted to mechanical energy")

class TestElectricToaster(unittest.TestCase):
    def test_toaster_appliance_not_empty(self):
        not_empty = self.toaster = Toaster
        self.assertTrue(not_empty, True)

    def test_toaster_energy_conversion(self):
        toaster = Toaster()
        self.assertEqual(toaster.convert_energy(), "Electrical energy is converted to thermal energy")

class TestCooker(unittest.TestCase):
    def test_cooker_appliance_not_empty(self):
        not_empty = self.cooker = Cooker
        self.assertTrue(not_empty, True)

    def test_cooker_energy_conversion(self):
        cooker = Cooker()
        self.assertEqual(cooker.convert_energy(), "Electrical energy is converted to heat energy")

class TestBlender(unittest.TestCase):
    def test_blender_appliance_not_empty(self):
        not_empty = self.blender = Blender
        self.assertTrue(not_empty, True)

    def test_blender_energy_conversion(self):
        blender = Blender()
        self.assertEqual(blender.convert_energy(), "Electrical energy is converted to mechanical energy")

class TestSpeaker(unittest.TestCase):
    def test_speaker_appliance_not_empty(self):
        not_empty = self.speaker = Speaker
        self.assertTrue(not_empty, True)

    def test_speaker_energy_conversion(self):
        speaker = Speaker()
        self.assertEqual(speaker.convert_energy(), "Electrical energy is converted to sound energy")

class TestNaturalGas(unittest.TestCase):
    def test_natural_gas_appliance_not_empty(self):
        not_empty = self.natural_gas = NaturalGas
        self.assertTrue(not_empty, True)

    def test_natural_gas_energy_conversion(self):
        natural_gas = NaturalGas()
        self.assertEqual(natural_gas.convert_energy(), "Chemical energy is converted into thermal energy")


