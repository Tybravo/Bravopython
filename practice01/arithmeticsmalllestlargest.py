#Question 10

numberone = int(input("Enter first number: "))
numbertwo = int(input("Enter second number: "))
numberthree = int(input("Enter third number: "))


sum = numberone + numbertwo + numberthree
average = (numberone + numbertwo + numberthree) / 3
product = numberone * numbertwo * numberthree

print(sum)
print(average)
print(product)


if numberone > numbertwo and numberone > numberthree:
 print(numberone, "is the largest number")

if numbertwo > numberone and numbertwo > numberthree:
 print(numbertwo, "is the largest number")

if numberthree > numberone and numberthree > numbertwo:
 print(numberthree, "is the largest number")


if numberone < numbertwo and numberone < numberthree:
 print(numberone, "is the smallest number")

if numbertwo < numberone and numbertwo < numberthree:
 print(numbertwo, "is the smallest number")

if numberthree < numberone and numberthree < numbertwo:
 print(numberthree, "is the smallest number")





