def character_occurrence(word):

    get_character = {}
    for character in word:
        get_character[character] = word.count(character)
    if not []:
        return get_character

print(character_occurrence("Adetayo"))

