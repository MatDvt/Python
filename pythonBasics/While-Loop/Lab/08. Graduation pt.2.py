name = input()
counter = 0
fails = 0
total_grades = 0

while counter < 12:
    grade = float(input())
    if grade >= 4:
        counter += 1
        fails = 0
        total_grades += grade
    else:
        fails += 1

    if fails == 2:
        print(f'{name} has been excluded at {counter + 1} grade')
        break
if counter == 12:
    print(f'{name} graduated. Average grade: {total_grades / 12:.2f}')
