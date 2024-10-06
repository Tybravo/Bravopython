import string

def list2_object(numbers):
    value = {}

    #numbers = numbers.append(numbers)
    #numbers = ''.join(numbers)
    space = ""
    num = map(str, numbers)
    numbers = space.join(num)

    print(numbers)

    for number in numbers:
        value[number] = numbers.count(number)
        print(value)
        return value

print(list2_object([1,1,2,3,2]))




##################################################################################

def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = int("".join(s))

    return (res)


input = [200]

# Using map
output = list(map(int, str(input[0])))

# Printing output
print(output)

list = [1, 2, 3]
print(convert(list))



