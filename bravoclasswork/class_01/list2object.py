import string
def list2_object(numbers):
    value = {}

    for data in numbers:
        value[data] = numbers.count(data)
    if not []:
        return value

print(list2_object([1,1,2,3,2]))




