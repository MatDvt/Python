def chars_to_string_in_asci(ch1, ch2):
    # create a list from the chars and represent their ASCI value
    list_of_chars = [chr(x) for x in range(ord(ch1), ord(ch2) + 1)]

    # remove the start and end value in the list
    list_of_chars.pop(0)
    list_of_chars.pop(-1)

    # empty var to use as separator
    delimiter = ' '

    # convert the list to string using list(map())
    list_of_chars = list(map(str, list_of_chars))
    final_list = delimiter.join(list_of_chars)

    return final_list


char1 = input()
char2 = input()
print(chars_to_string_in_asci(char1, char2))
