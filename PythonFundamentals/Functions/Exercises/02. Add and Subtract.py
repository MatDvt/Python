def sum_numbers(n1, n2):
    res = n1 + n2
    return res


def subtract(res, n3):
    return res - n3


def add_and_subtract(number1, number2, number3):
    sums = sum_numbers(number1, number2)
    subs = subtract(sums, number3)
    return subs


num1 = int(input())
num2 = int(input())
num3 = int(input())
result = add_and_subtract(num1, num2, num3)
print(result)
