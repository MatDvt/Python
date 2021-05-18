def exchange(nums_list, index):
    first_part = nums_list[index + 1:]
    second_part = nums_list[:index + 1]
    result = first_part + second_part
    return result


def find_max_num(nums_list, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)
    if not filtered_nums:
        return "No matches"
    max_element = max(filtered_nums)

    index = len(filtered_nums) - filtered_nums[::-1].index(max_element) - 1
    return index


def find_min_num(nums_list, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums:
        return "No matches"
    max_element = min(filtered_nums)
    index = len(filtered_nums) - filtered_nums[::-1].index(max_element) - 1
    return index


def find_first(nums_list, count, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        for el in nums_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in nums_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if len(filtered_nums) < count:
        return "Invalid count"
    return filtered_nums[:count]


nums_as_string = input().split()
nums = []

for el in nums_as_string:
    nums.append(int(el))

command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        i = int(command_data[1])
        nums = exchange(nums, i)
    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))
    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))
    elif command == "first":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(find_first(nums, count, odd_or_even))
    elif command == "last":
        pass

    command_data = input()