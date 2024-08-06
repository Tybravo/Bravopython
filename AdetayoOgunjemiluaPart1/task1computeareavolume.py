#prompt the user to enter radius and length of a cylinder
#read the user's inputed radius and length
#define the user's input and pie as constant
#multiply pie by radius raised to power of 2 to get the area
#multiply area by length to get the volume of the cylinder
#identify your results 1 as the area
#identify your result 2 as the length
#printhe  area
#print the length


radius = int(input("Enter the radius of the cylinder: "))
length = int(input("Enter the length of the cylinder: "))

PI = 3.142
isarea = pie * (radius ** 2)
isvolume = isarea * length

print("Area of the cylinder is ", isarea)
print("Length of the cylinder is ", isvolume)
