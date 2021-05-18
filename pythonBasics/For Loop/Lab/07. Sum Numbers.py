# •	От първия ред на входа се въвежда броят числа n.
# •	От следващите n реда се въвежда по едно цяло число.
# Програмата трябва да прочете числата, да ги сумира и да отпечата сумата им.

count = int(input())

result = 0
for i in range(count):
    number = int(input())
    result += number
print(result)
