def smallest_num(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    elif n3 < n1 and n3 < n2:
        return n3


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = smallest_num(num1, num2, num3)
print(result)