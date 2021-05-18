lst_ints = [int(x) for x in input().split(" ")]
n = int(input())

for num in range(n):
    lst_ints.remove(min(lst_ints))

print(lst_ints)
