# Given a string, you have to print a string in which each character (case-sensitive) is repeated.

word = input()

for char in word:
    dbl = (char * 2)
    print(dbl, end='')
