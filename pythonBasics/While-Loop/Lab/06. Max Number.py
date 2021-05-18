import sys

n = input()

max_num = -sys.maxsize

while n != 'Stop':
    number = int(n)
    if number > max_num:
        max_num = number
    n = input()
print(max_num)
