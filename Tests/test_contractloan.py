import unittest

from class_01 import contractloan

class TestContractLoan(unittest.TestCase):
    def setUp(self):
        self.loan = contractloan.ContractLoan("James", 0.15, 200_000, 2)

    def test_that_contract_loan_app_exist(self):
        exist = self.loan = contractloan.ContractLoan("James", 0.15, 200_000, 2)
        self.assertTrue(exist)

    def test_that_contract_loan_app_can_get_monthly_rate(self):
        monthly_rate = self.loan.get_monthly_rate()
        self.assertTrue(monthly_rate, 0.0125)

    def test_that_contract_loan_app_can_get_borrower_details(self):
        borrower = contractloan.ContractLoan("James", 0.15, 200_000, 2)
        self.assertEqual(borrower, "James", 0.0125)


