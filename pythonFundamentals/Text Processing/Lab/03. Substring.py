str_1 = input()
str_2 = input()

while str_1 in str_2:
    str_2 = str_2.replace(str_1, "")
print(str_2)
