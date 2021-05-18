string_of_nums = input().split(", ")
even_nums = [int(num) for num in string_of_nums]
# nums_map = list(map(lambda el: int(el), string_of_nums))
# nums_map_ref_to_function = list(map(int, string_of_nums))

filtered_nums = [index for index in range(len(even_nums)) if even_nums[index] % 2 == 0]

print(filtered_nums)
