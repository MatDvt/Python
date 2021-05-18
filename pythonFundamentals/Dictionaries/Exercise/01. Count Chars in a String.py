string = [c for c in input().replace(" ", "")]

chars = {}

for c in string:
    if c not in chars:
        chars[c] = 1
    else:
        chars[c] += 1
for key, value in chars.items():
    print(f"{key} -> {value}")
