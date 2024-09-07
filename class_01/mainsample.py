import numbers


"""
# LIST LEARNING
x = [[0 for _ in range(4)] for _ in range(5)]

#number = [0]
#x = [0]

for number in range(5):
    for fig in range(4):
         x[number][fig] = 8

print(x)

x = []
n = [0] * 4
for _ in range(5):
    x.append(n)
    
print(x)
"""


"""
# TUPLE AND LIST LEARNING
#list2 = (1, 2, 3)
score = (1, 2, 3, 4, "Bravo")
list2 = [1, 2, 3, "Adetayo", 2.5]
print(list2)
#list2[3] = "Adetayo"
#print(list2)
single_tuple = 1,
print(score[3])

score = list(score)
score[4] = "Bravo"
score = tuple(score)
print(score)
print(type(score))


tuple2 = (1, 2, 3, [2, 4, 6], "priest", "10.3")
print(tuple2)
tuple2[3].extend([8, 10])
print(tuple2)
print(len(tuple2))
"""


student3  = {
    "first_name": "Bolaji",
    "last_name": "Bravo",
    "gender": "Male",
    "age": "24",
    "grade": {
        "maths": "67",
        "english": "78",
        "physics": "88",
    }
}


print(student3)

lists = list(range(1, 51))

a, b, c = lists[0], lists[1], lists[2]
print(lists)
print(a, b, c)
