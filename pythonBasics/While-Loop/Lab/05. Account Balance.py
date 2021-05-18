command = input()

total_sum = 0

while command != 'NoMoreMoney':
    money = float(command)
    if money <= 0:
        print('Invalid operation!')
        break
    else:
        total_sum += money
        print(f'Increase: {money:.2f}')
        command = input()
print(f'Total: {total_sum:.2f}')
