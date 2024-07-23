
print(""" 0 Single Filers
 1 Married Filing Jointly
 2 Married Filing Separately
 3 Head of Household """)

filingstatus = int(input("Enter between 0 and 3 for your filling status: "))
personalincometax = 0;

match filingstatus:
	case 0:
		taxableincome = int(input("Enter your taxable income: "))
		if taxableincome > 0 and taxableincome <= 8350:
			personalincometax = taxableincome * (10/100)
		elif taxableincome >= 8351 and taxableincome <= 33950:
			personalincometax = taxableincome * (15/100)
		elif taxableincome >= 33951 and taxableincome <= 82250:
			personalincometax = taxableincome * (25/100)
		elif taxableincome >= 82251 and taxableincome <= 171550:
			personalincometax = taxableincome * (28/100)
		elif taxableincome >= 171551 and taxableincome <= 372950:
			personalincometax = taxableincome * (33/100)
		elif taxableincome >= 372951:
			personalincometax = taxableincome * (35/100)
		print("Income tax for amount entered as Single Filers is ", personalincometax)

	case 1:
		taxableincome = int(input("Enter your taxable income: "))
		if taxableincome >0 and taxableincome <= 16700:
			personalincometax = taxableincome * (10/100)
		elif taxableincome >= 16701 and taxableincome <= 67900:
			personalincometax = taxableincome * (15/100)
		elif taxableincome >= 67901 and taxableincome <= 137050:
			personalincometax = taxableincome * (25/100)
		elif taxableincome >= 137051 and taxableincome <= 208850:
			personalincometax = taxableincome * (28/100)
		elif taxableincome >= 208851 and taxableincome <= 372950:
			personalincometax = taxableincome * (33/100)
		elif taxableincome >= 372951:
			personalincometax = taxableincome * (35/100)
		print("Income tax for amount entered as Married Filing Jointly is ", personalincometax)

	case 2:
		taxableincome = int(input("Enter your taxable income: "))
		if taxableincome > 0 and taxableincome <= 8350:
			personalincometax = taxableincome * (10/100)
		elif taxableincome >= 8351 and taxableincome <= 33950:
			personalincometax = taxableincome * (15/100)
		elif taxableincome >= 33951 and taxableincome <= 68525:
			personalincometax = taxableincome * (25/100)
		elif taxableincome >= 68526 and taxableincome <= 104425:
			personalincometax = taxableincome * (28/100)
		elif taxableincome >= 104426 and taxableincome <= 186475:
			personalincometax = taxableincome * (33/100)
		elif taxableincome >= 186476:
			personalincometax = taxableincome * (35/100)
		print("Income tax for amount entered as Married Filing Separately is ", personalincometax)

	case 2:
		taxableincome = int(input("Enter your taxable income: "))
		if taxableincome > 0 and taxableincome <= 11950:
			personalincometax = taxableincome * (10/100)
		elif taxableincome >= 11951 and taxableincome <= 45500:
			personalincometax = taxableincome * (15/100)
		elif taxableincome >= 45501 and taxableincome <= 117450:
			personalincometax = taxableincome * (25/100)
		elif taxableincome >= 117451 and taxableincome <= 190200:
			personalincometax = taxableincome * (28/100)
		elif taxableincome >= 190201 and taxableincome <= 372950:
			personalincometax = taxableincome * (33/100)
		elif taxableincome >= 372951:
			personalincometax = taxableincome * (35/100)
		print("Income tax for amount entered as Head of Household is ", personalincometax)


