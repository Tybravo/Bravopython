#prompt the user to enter integer between 0 and 1000
#collect the 3 integers
#split the 3 integers into each digits using // and % operator
#add the digits to get sum
#identity the result as sum
#print to display sum


collectnum =  int(input("Enter integers between 0 and 1000 :"))

digitone = collectnum // 100
digittwo = collectnum // 10 % 10
digitthree = collectnum % 10

sumofdigits = digitone + digittwo + digitthree

print("Sum of digits is ", sumofdigits)

