seq_of_strings = input()

lst_of_the_strings = []

dic_of_strings = {}

while not seq_of_strings == "stop":
    lst_of_the_strings.append(seq_of_strings)
    seq_of_strings = input()

for index in range(0, len(lst_of_the_strings), 2):
    product = lst_of_the_strings[index]
    value = int(lst_of_the_strings[index + 1])

    if product not in dic_of_strings:
        dic_of_strings[product] = value
    else:
        dic_of_strings[product] += value
for key, val in dic_of_strings.items():
    print(f"{key} -> {val}")
