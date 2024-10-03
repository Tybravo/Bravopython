import unittest
import re
from class_01 import passwgen


class TestPasswordgenerator(unittest.TestCase):
    def test_password_generator_exist(self):
        exist = passwgen.passw_gen()
        self.assertTrue(exist)

    def test_password_generator_ingredient_length(self):
        value = passwgen.passw_gen().split()
        print(f'value: ',value)
        generated_password = value[0]
        collect_number = value[1]
        collect_lower_letter = value[2]
        collect_upper_letter = value[3]
        collect_symbol = value[4]

        generated_password = len(generated_password) == 18
        self.assertTrue(generated_password)

        collect_number = int(collect_number) == 5
        self.assertTrue(collect_number)

        collect_lower_letter = int(collect_lower_letter) == 5
        self.assertTrue(collect_lower_letter)

        collect_upper_letter = int(collect_upper_letter) == 5
        self.assertTrue(collect_upper_letter)

        collect_symbol = int(collect_symbol) == 3
        self.assertTrue(collect_symbol)

    def test_password_generator_password_valid_regrex(self):
        valid = passwgen.passw_gen()
        given = re.fullmatch(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[\W_]).+$', valid)
        self.assertTrue(given, valid)

