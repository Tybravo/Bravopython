
class ContractLoan:

    def __init__(self, borrower, annual_rate, loan_amount, loan_period, number_of_months = 12):
        self.borrower = borrower
        self.annual_rate = annual_rate
        self.loan_amount = loan_amount
        self.loan_period = loan_period
        self.number_of_months = number_of_months

    def __str__(self):
        return (f"Borrower: {self.borrower}\n"
                f"Annual Rate: {self.annual_rate}\n"
                f"Loan Amount: {self.loan_amount}\n"
                f"Loan Period (years): {self.loan_period}\n"
                f"Number of Months: {self.number_of_months}")

    @property
    def get_borrower_loan_details(self):
        borrower = ContractLoan("Michael Bravo", 0.15, 200_000, 2)
        return borrower

    def get_monthly_rate(self):
        monthly_rate = self.annual_rate / self.number_of_months
        return round(monthly_rate, 4)

    def get_monthly_duration(self):
        monthly_duration = self.loan_period * 12
        return monthly_duration

    def get_monthly_payment(self):
        monthly_rate  = self.get_monthly_rate()
        monthly_duration = self.get_monthly_duration()

        numerator = self.loan_amount * monthly_rate
        denominator = 1-(1/(1+monthly_rate) ** monthly_duration)
        monthly_payment = numerator / denominator
        return round(monthly_payment, 2)

    @staticmethod
    def get_total_payment(monthly_payment, monthly_duration):
        total_payment = monthly_payment * monthly_duration
        return round(total_payment, 0)


loan = ContractLoan("Michael Bravo", 15, 200_000, 2)

print(loan)



print(loan.annual_rate)

print(loan.get_monthly_rate())

print(loan.get_monthly_payment())

print(loan.get_total_payment(9697.33, 24))






