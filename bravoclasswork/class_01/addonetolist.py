def add_one(numbers):

    split_number = []


    #numbers = str(numbers)
    get_numbers = [str(index) for index in numbers]


    #for index in numbers:
        #get_numbers = numbers
        #split_number.append(get_numbers)
    num_int = int("".join(get_numbers))

    total_num = num_int + 1

    total_num = str(total_num)
    for number in total_num:
        #split_number += number
        split_number.append(int(number))
    #list(map(int, str(total_num[0])))

    return split_number

print(add_one([1,4,7]))