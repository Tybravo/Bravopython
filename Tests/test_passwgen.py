import unittest

from class_01 import passwgen

class TestPasswordgenerator(unittest.TestCase):
    def test_password_generator_exist(self):
        exist = passwgen.passw_gen()
        self.assertTrue(exist)