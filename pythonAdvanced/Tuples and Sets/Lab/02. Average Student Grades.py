n = int(input())

students = {}

for _ in range(n):
    data = tuple(input().split())
    student_name, grade = data
    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(grade))

for key, value in students.items():
    print(f'{key} -> {value}')