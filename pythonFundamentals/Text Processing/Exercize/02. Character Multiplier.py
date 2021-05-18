string1, string2 = input().split()
sum = 0
length1 = len(string1)
length2 = len(string2)
strings_number = 0
while length1 != 0 and length2 != 0:
    sum += ord(string1[strings_number]) * ord(string2[strings_number])
    strings_number += 1
    length1 -= 1
    length2 -= 1
if length1 == 0 and length2 == 0:
    sum = sum
elif length1 == 0:
    ordenanza = 0
    for chara in range(length2):
        ordenanza -= 1
        sum += ord(string2[ordenanza])
elif length2 == 0:
    ordenanza = 0
    for chara in range(length1):
        ordenanza -= 1
        sum += ord(string1[ordenanza])
print(sum)
