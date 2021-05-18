employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())

students_count = int(input())

all_employee_student_per_h = employee_1 + employee_2 + employee_3
needed_hours = 0

while students_count > 0:
    students_count -= all_employee_student_per_h
    needed_hours += 1
    if needed_hours % 4 == 0:
        needed_hours += 1

print(f'Time needed: {needed_hours}h.')