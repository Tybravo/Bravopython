from contextlib import nullcontext


def count_evenodd(even_and_odd):
    # get_numbers = int([2,1,5,7,8])
    get_numbers = []
    count_even = 1
    count_odd = 0
    for number in even_and_odd:
        if number % 2 == 0:
            count_even = count_even +1
        if number % 2 == 1:
            count_odd = count_odd+1

            get_numbers = [count_even, count_odd]
    return get_numbers




print(count_evenodd([2,1,5,7,8]))