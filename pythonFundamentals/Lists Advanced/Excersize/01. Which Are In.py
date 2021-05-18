substrings = input().split(", ")
words = input().split(", ")

which_are_in = []

for sub in substrings:
    for word in words:
        if sub in word:
            which_are_in.append(sub)
print(sorted(set(which_are_in), key=which_are_in.index))
