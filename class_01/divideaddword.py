def divide_add_word(word):
    get_word = "helloo"
    get_word2 = "joy"

    if len(word) % 2 == 0:
        average = len(word) // 2
        get_word_one = word[:average]
        get_word_two = word[average:]
        get_word = get_word_one + "ce" + get_word_two

        return get_word

    elif len(word) % 2 != 0:
        get_word = word + "ce"

        return get_word


print(divide_add_word("helloo"))
print(divide_add_word("joy"))
