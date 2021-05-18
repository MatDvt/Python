import sys

n = input()

min_num = sys.maxsize

while n != 'Stop':
    number = int(n)
    if number < min_num:
        min_num = number
    n = input()
print(min_num)
