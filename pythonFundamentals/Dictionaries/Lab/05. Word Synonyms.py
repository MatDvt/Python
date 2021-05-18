n = int(input())

synonyms = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in synonyms:
        synonyms[word] = []  # правим празен лист вътре в речника ако го не е
    synonyms[word].append(synonym)  # ако го има, добавяме към вече създадения лист следващия синоним

for key, values in synonyms.items():
    print(f"{key} - {', '.join(values)}")
