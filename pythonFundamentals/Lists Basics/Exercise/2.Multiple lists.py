factor = int(input())
count = int(input())

numbers = []

for i in range(factor, factor * count + 1, factor):
    numbers.append(i)
print(numbers)
