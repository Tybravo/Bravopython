
isprincipal = int(input("Enter the principal amount: "))
israte = int(input("Enter the the amount interest rate: "))
isduration = int(input("Enter the duration in years: "))

israte = israte / 100 / 12

ismonthly = isduration * 12

numerate = israte * (1 + israte)**ismonthly
denominate = (1 +  israte)**ismonthly - 1

monthlypayment = isprincipal * (numerate / denominate)

print("Your monthly payment is ", monthlypayment)





