words = [el.strip() for el in input().split(" ")]

all_sum = 0

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"

for word in words:

    if len(word) == 0:
        continue
    for i in range(len(word)):
        result = 0
        first_letter = word[0]
        last_letter = word[-1]
        number = int(word[1:-1])
        if first_letter.isupper():
            index = int(upper.find(first_letter) + 1)
            result = number / index
        else:
            index = int(lower.find(first_letter) + 1)
            result = number * index
        if last_letter.isupper():
            index = int(upper.find(last_letter) + 1)
            result = result - index
            all_sum += result
            break

        else:
            index = int(lower.find(last_letter) + 1)
            result = result + index
            all_sum += result
            break

print(f"{all_sum:.2f}")
