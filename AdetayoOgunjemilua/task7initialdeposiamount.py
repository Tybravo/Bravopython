#prompt the user to enter number of minutes
#collect the user inputs

#declare the annual rate
#declare the monthly rate
#declare the amount need to deposit after 3 years
#divide final account value by 1 + monthly interest rate  raised to power number of months


anunal_interestrate = 4.25 / 100
monthly_interestrate = anunal_interestrate / 12
number_of_month = 12 * 3

initial_deposit_amount = 5000 / ((1 + monthly_interestrate) * number_of_month)

print("Initial deposit amount is ", initial_deposit_amount)

