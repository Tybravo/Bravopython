def swap_string_add(string1, string2):
    # string1 = "abc"
    # string2 = "xyz"
    get_string1 = string2[:2] + string1[2:]
    get_string2 = string1[:2] + string2[2:]

    concat_string = get_string1+" "+ get_string2

    return concat_string



print(swap_string_add("abc","xyz"))

