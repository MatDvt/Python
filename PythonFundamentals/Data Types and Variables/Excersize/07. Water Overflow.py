# n = int(input())
#
# tank_capacity = 255
# current_capacity = 0
#
# for i in range(1, n + 1):
#     liters = int(input())
#     current_capacity += liters
#     tank_capacity -= current_capacity
#     if liters > tank_capacity:
#         print(f'Insufficient capacity!')
#
#
# print(current_capacity)

TANK_CAPACITY = 255
current_tank_capacity = 0
n = int(input())

for _ in range(1, n +1):
    liters = int(input())

    if current_tank_capacity + liters > TANK_CAPACITY:
        print(f'Insufficient capacity!')
    else:
        current_tank_capacity += liters
print(current_tank_capacity)