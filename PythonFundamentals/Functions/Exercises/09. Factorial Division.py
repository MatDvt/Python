import math


def fact_division(n1, n2):
    n1_fact_result = math.factorial(n1)
    n2_fact_result = math.factorial(n2)

    result = n1_fact_result / n2_fact_result
    return f"{result:.2f}"


first_num = int(input())
second_num = int(input())
print(fact_division(first_num, second_num))
