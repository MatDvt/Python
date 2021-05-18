num_of_chars = int(input())

ascii_char = ''
sum_ascii = 0
for letter in range(num_of_chars):
    char = str(input())
    ascii_char = ord(char)
    sum_ascii += int(ascii_char)

print(f'The sum equals: {sum_ascii}')
