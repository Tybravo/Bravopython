#Question 11



numdigit = int(input("Enter five digit numbers to seperate them: "))

getfirstdigit = numdigit // 10000
getfifthdigit = numdigit % 10

togetseconddigit = numdigit // 1000
getseconddigit = togetseconddigit % 10

togetthirddigit = numdigit // 100
getthirddigit = togetthirddigit % 10

togetfourthdigit = numdigit // 10
getfourthdigit  = togetfourthdigit % 10

print(getfirstdigit,  getseconddigit,  getthirddigit,  getfourthdigit,  getfifthdigit)

