n = int(input())

chemicals = set()

for _ in range(n):
    chemicals = chemicals.union(set(input().split()))

for el in chemicals:
    print(el)