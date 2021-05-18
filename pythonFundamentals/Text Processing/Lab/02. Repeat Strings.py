data = input().split()
result = ""

for s in data:
    result += s * len(s)
print(result)
