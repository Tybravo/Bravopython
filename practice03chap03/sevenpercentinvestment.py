#Question 3.10



principal = int(1000)

for count in range(1, 31):
	returnamount = principal * (1 + 7/100)**count
	
	print("Investment return for year "+str(count)+" is $",f' {returnamount:.2f} ')	
  
