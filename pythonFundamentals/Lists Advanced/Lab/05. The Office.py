employees_happiness_as_string = [int(num) for num in input().split(" ")]
happiness_factor = int(input())

multi_employees_happiness = [happiness * happiness_factor for happiness in employees_happiness_as_string]

average_happiness = sum(multi_employees_happiness) // len(multi_employees_happiness)

filtered_empl = list(filter(lambda employee: employee > average_happiness, multi_employees_happiness))
half_n = len(multi_employees_happiness) // 2

if len(filtered_empl) >= half_n:
    print(f'Score: {len(filtered_empl)}/{len(multi_employees_happiness)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_empl)}/{len(multi_employees_happiness)}. Employees are not happy!')
# print(len(filtered_empl))



