def not_vowel(character):
    if character not in "aeouei":
        return True
    return False

print("".join([char for char in input() if not_vowel(char)]))

