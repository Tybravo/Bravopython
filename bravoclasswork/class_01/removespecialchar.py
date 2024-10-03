def remove_special_char(word_char):

    word_char = "he.ll,o"
    get_word_char = word_char.replace(".","")
    get_word_char = get_word_char.replace(",", "")

    return get_word_char

print(remove_special_char("he.ll,o"))
