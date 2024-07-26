#prompt the user to enter gratuity rate
#prompt the user to enter subtotal
#read gratuity rate
#read subtotal rate
#multiply the gratuity rate by the subtotal to get the gratuity
#sum the result gotten from the gratuity and the collected subtotal to get the total
#print to display the gratuity 
#print to display the total

subtotal = int(input("Enter subtotal :"))
gratuityrate = int(input("Enter gratuity rate :"))

gratuity = (gratuityrate / 100) * subtotal
total = gratuity + subtotal

print("Gratuity is ", gratuity)
print("Total is ", total)



