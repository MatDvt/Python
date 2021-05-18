course_data = input().split(" : ")
data_courses = {}

while not course_data[0] == 'end':

    course = course_data[0]
    student = course_data[1]

    if course not in data_courses:
        data_courses[course] = [student]
    else:
        data_courses[course].append(student)

    course_data = input().split(" : ")

# sorting the courses by how many students it has
sorted_items = sorted(data_courses.items(), key=lambda kvp: -len(kvp[1]))

for key, value in sorted_items:
    print(f"{key}: {len(value)} ")
    value = sorted(value)  # sorting the values only alphabetically
    for val in value:
        print(f"-- {val}")
