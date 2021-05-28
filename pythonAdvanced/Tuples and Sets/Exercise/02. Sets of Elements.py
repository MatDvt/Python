n, m = input().split()
n, m = int(n), int(m)

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())

present_IN_both = n_set.intersection(m_set)
for el in present_IN_both:
    print(el)


# for element in n_set:
#     if element in m_set:
#         print(element)
