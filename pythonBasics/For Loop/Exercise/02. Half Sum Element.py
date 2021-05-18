import sys

n = int(input())

max_num = -sys.maxsize
sum_num = 0

for i in range(0, n):
    num = int(input())

    if num > max_num:
        max_num = num

    sum_num += num

other_sum = sum_num - max_num

if other_sum == max_num:
    print(f'Yes\nSum = {max_num}')
else:
    print(f'No \nDiff = {abs(max_num - other_sum)}')
