exp_to_decipher = input().split()

for word in exp_to_decipher:
    num = ''  # take the num from within the string
    for char in word:
        if char.isdigit():
            num += char
    first_letter = chr(int(num))
    current_word = first_letter + word[len(num):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    print(f"{''.join(current_word)}", end=" ")
