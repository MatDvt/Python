import math

persons = int(input())
capacity = int(input())

course_calculate = math.ceil(persons / capacity)

print(course_calculate)
