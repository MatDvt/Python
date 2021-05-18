n = int(input())

result = 0
result_1 = 0

for i in range(n):
    number = int(input())
    result += number
for i in range(n):
    number1 = int(input())
    result_1 += number1

if result == result_1:
    print(f'Yes, sum = {result}')
else:
    print(f'No, diff = {abs(result - result_1)}')

# elif result > result_1:
#    diff = result - result_1
#    print(f'No, diff = {diff}')
# elif result_1 > result:
#    diff= result_1 - result
#    print(f'No, diff = {diff}')
