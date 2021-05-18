import sys

kozunaci = int(input())
name = input()
grade = int(input())

max_points = -sys.maxsize
sum_points = 0
current_baker_max_points = ''

for i in range(1, kozunaci + 1):
    grade = int(input())

    while name != 'Stop':

        sum_points += grade
        if sum_points > max_points:
            max_points = sum_points
            current_baker_max_points = name

        grade = int(input())
    name = input()

    if name == 'Stop':
        print(f'{name} has {sum_points} points.')
