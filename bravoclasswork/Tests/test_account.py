from unittest import TestCase
from class_01.accountsample import Account


class TestAccount(TestCase):

    def test_that_account_exist(self):
        acc1 = Account("John", "0000", 0)

    def test_that_account_balance_Zero (self):
        acc1 = Account("John", "0000",0)
        self.assertEqual(acc1.balance, 0.00)

    def test_that_account_can_deposit(self):
        acc1 = Account("John", "0000", 0)
        acc1.deposit(10_000)
        acc1.deposit(5_000)
        self.assertEqual(acc1.balance, 15_000)

    def test_account_cannot_deposit_negative(self):
        acc1 = Account("John", "0000", 0)
        acc1.deposit(1000)
        acc1.deposit(-2000)
        self.assertEqual(acc1.balance, 1000)





