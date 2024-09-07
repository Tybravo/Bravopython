def gettuple(tuple2):

    #getitem = tuple2[0]

    tuple2 = ("Orange", [10, 20, 30],(5, 15, 25))
    #item = list(tuple2)
    getlist1= tuple2[1]
    getlist2 = tuple2[2]

    getnumber = [getlist1[1], getlist2[2]]

    takeist1 = tuple2[1][1]
    takeist2 = tuple2[2][2]

    tuple_element =  ((0, takeist1), (1, takeist2))



    return tuple_element

print(gettuple("tuple_element"))