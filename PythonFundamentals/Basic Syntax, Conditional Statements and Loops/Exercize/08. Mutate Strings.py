# You will be given two strings.
# #Transform the first string into the second one, one letter at a time and print it.
# #Print only the unique strings
# Note: the strings will have the same lengths


str_1 = input()
str_2 = input()

result = ""
previous_str = str_1

for index in range(len(str_1)):
    for i in range(index+1):
        result += str_2[i]
    for j in range(index+1, len(str_2)):
        result += str_1[j]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""
