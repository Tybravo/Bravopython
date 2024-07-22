
def my_discount(price, discount):

	actualprice = (discount / 100) * price
	discountedprice = price - actualprice
	
	return f" The discounted price is {discountedprice} "

print(my_discount(150, 15))
print(my_discount(290, 10))

