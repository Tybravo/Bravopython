import unittest

from class_01 import emailvalidation

class TestEmailValidation(unittest.TestCase):
    def test_that_email_is_valid(self):
        valid = emailvalidation.validate_email("Tybravo@home.com")
        self.assertFalse(False)
