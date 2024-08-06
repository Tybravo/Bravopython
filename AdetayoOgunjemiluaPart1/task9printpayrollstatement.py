
employee_name = input("Enter employee name: ")
hours_perweek = int(input("Enter number of hours in a week: "))
hourly_payrate = float(input("Enter hourly pay rate: "))
federaltax_withholdingrate = float(input("Enter Federal tax withholding rate: "))
statetax_withholdingrate = float(input("Enter State tax withholding rate: "))

grossspayrate = hourly_payrate * hours_perweek

federalwithholding = federaltax_withholdingrate * grossspayrate
statewithholding = statetax_withholdingrate * grossspayrate

totaldeduction = federalwithholding + statewithholding
netpay = grossspayrate - totaldeduction

print("Gross Pay", grossspayrate, "\nFederal Withholding", federalwithholding, "\nState Withholding", statewithholding, "\nTotal Deduction", totaldeduction, "\nNet Pay", netpay)










