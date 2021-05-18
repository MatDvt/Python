# If you can't sleep, just count sheep! Given a non-negative integer,
# #3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep..."
# #Input will always be valid, i.e. no negative integers.

num = int(input())

for sheep in range(1, num+1):
    print(f'{sheep} sheep...', end='')
