n = int(input())

odd_sum = 0
even_sum = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
if even_sum == odd_sum:
    print(f'Yes \nSum = {odd_sum}')
# print(f'Sum = {odd_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')
