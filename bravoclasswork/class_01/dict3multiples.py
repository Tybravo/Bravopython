def list_to_dict_pow(list):

    return {number: number ** 3 for number in list}
"""
    result = {}
    for number in list:
        result[number] = number ** 3
        return result
"""
print(list_to_dict_pow([1, 2, 3]))