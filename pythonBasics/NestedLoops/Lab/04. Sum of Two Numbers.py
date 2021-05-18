start_num = int(input())
end_num = int(input())
magic_num = int(input())

combination = 0
is_found = False  # проверяваме кога имаме валидна комбинация

for first in range(start_num, end_num + 1):
    for second in range(start_num, end_num + 1):
        combination += 1
        if first + second == magic_num:
            is_found = True
            print(f'Combination N:{combination} ({first} + {second} = {magic_num})')
            break
        #  sys.exit()  # може да прекратим цялата програма(и двате фор-а и двате break-a ще са излишни
    if is_found:
        break

if not is_found:
    print(f'{combination} combinations - neither equals {magic_num}')
