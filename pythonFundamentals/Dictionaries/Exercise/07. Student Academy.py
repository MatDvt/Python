n_rows = int(input())

grades_students = {}

for rows in range(n_rows):
    student = input()
    grade = float(input())

    if student not in grades_students:
        grades_students[student] = []  # an empty list for the grades of every student
    grades_students[student].append(grade)

filtered_grades = {}  # a separate dict for the ones with higher grades

for student_name, grades in grades_students.items():
    avg_grade = sum(grades) / len(grades)
    if avg_grade >= 4.5:
        filtered_grades[student_name] = avg_grade

sorted_students = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1]) #sorting by the grades descending

for std, grd in sorted_students:
    print(f"{std} -> {grd:.2f}")
