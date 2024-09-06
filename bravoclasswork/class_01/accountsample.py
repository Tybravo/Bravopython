from decimal import Decimal

class Account:

    def __init__(self, name: str, pin: str, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > Decimal(0.00):
          #raise ValueError(f"{amount} is an Invalid amount")
            self.balance += amount

        if amount < Decimal(0.00):
            return self.balance
       #else return self.balance






# account1 = Account("Adetayo", "1111", 0)
# account2 = Account( "Mike",  "0000",0)
#
