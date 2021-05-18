# Write a program to read an integer n and print all triples of the first n small Latin letters, ordered alphabetically:

num = int(input())

for i in range(0, num):
    for k in range(0, num):
        for j in range(0, num):
            print(f'{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}')
