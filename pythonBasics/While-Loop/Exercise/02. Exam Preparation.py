bad_grades_count = int(input())
grade_count = 0
grade_sum = 0
task_count = 0
last_task_name = ''
counter = 0
task_name = input()
while task_name != 'Enough':
    grade = int(input())
    grade_sum += grade
    grade_count += 1
    task_count += 1
    last_task_name = task_name
    if grade <= 4:
        counter += 1
    if counter == bad_grades_count:
        print(f'You need a break, {bad_grades_count} poor grades.')
        break
    task_name = input()

if task_name == 'Enough':
    print(f'Average score: {grade_sum / grade_count:.2f}')
    print(f'Number of problems: {task_count}')
    print(f'Last problem: {last_task_name}')

# It can be added here as well since this will mean that we are still in the while loop
# else:
#    print(f'You need a break, {bad_grades_count} poor grades.')
