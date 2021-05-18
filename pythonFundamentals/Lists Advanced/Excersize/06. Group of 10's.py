lst_of_numbers = [int(num) for num in input().split(", ")]

group = 10

while lst_of_numbers:
    nums_grp = []

    for num in lst_of_numbers:
        if num in range(group - 10, group + 1):
            nums_grp.append(num)
    for num in nums_grp:
        lst_of_numbers.remove(num)

    print(f"Group of {group}'s: {nums_grp}")
    group += 10
