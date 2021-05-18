n = int(input())

evens = []
odds = []
negatives = []
positives = []

for _ in range(n):
    nums = int(input())
    if nums % 2 == 0:
        evens.append(nums)
    if nums % 2 == 1:
        odds.append(nums)
    if nums < 0:
        negatives.append(nums)
    if nums >= 0:
        positives.append(nums)

command = input()

if command == "even":
    print(evens)
elif command == "odd":
    print(odds)
elif command == "positive":
    print(positives)
elif command == "negative":
    print(negatives)
