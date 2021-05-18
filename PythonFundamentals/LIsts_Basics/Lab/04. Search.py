num = int(input())
word = input()

list_1 = []
list_2 = []

for n in range(num):
    current_word = input()
    list_1.append(current_word)
    if word in current_word:
        list_2.append(current_word)
print(list_1)
print(list_2)