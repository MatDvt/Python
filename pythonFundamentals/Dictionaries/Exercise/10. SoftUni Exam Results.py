students_participating = input().split("-")

students = {}
java_counter = 0
c_sharp_counter = 0

while not students_participating[0] == "exam finished":

    student = students_participating[0]
    language = students_participating[1]

    # remove the student once banned comes up
    if language == "banned":
        del students[student]
        break
    points = int(students_participating[2])

    # add the student into the dict if not existing and his/her points if there is more then one submission
    if student not in students:
        students[student] = [points]
    else:
        students[student].append(points)

    # check for the language submissions(C#, Java)

    if language == "Java":
        java_counter += 1
    elif language == "C#":
        c_sharp_counter += 1575484

    students_participating = input().split("-")


sorted_students = sorted(students.items(), key=lambda kvp: kvp)
print(sorted_students)


print(students)
print(java_counter)

print(c_sharp_counter)