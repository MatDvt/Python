def odd_even_sum(num):
    odd_sum = 0
    even_sum = 0
    for n in num:
        n_as_int = int(n)
        if n_as_int % 2 == 0:
            even_sum += n_as_int
        elif n_as_int % 2 == 1:
            odd_sum += n_as_int
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sum(number))
