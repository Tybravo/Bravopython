#mutable and Imutable data type

#String object is imutable (changing)
name = "Temitope"
print(id(name))

name = name + ' Ayo'
print(id(name))


#Int Object is imutable (not changing)
number = 1
print(id(number))

number = number + 4
print(id(number))
print(number)


#List object is mutable
basket = [1, 2, 3, 4, 5]
print(id(basket))
basket.append(5)
print(id(basket))
print(basket)
