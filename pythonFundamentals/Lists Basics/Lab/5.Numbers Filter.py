# Using functions

number = int(input())

all_nums = []
filtered = []


def add_nums(n):
    for i in range(n):
        cur_n = int(input())
        all_nums.append(cur_n)


add_nums(number)

command = input()


def filter_nums(expression):
    for n in all_nums:
        if expression == 'even' and n % 2 == 0:
            filtered.append(n)
        elif expression == "odd" and n % 2 != 0:
            filtered.append(n)
        elif expression == "negative" and n < 0:
            filtered.append(n)
        elif expression == "positive" and n >= 0:
            filtered.append(n)
    print(filtered)


filter_nums(command)

# Without functions

# number = int(input())
#
# all_nums = []
# filtered = []
# for num in range(number):
#     cur_num = int(input())
#     all_nums.append(cur_num)
#
# command = input()
# for n in all_nums:
#     if command == 'even' and n % 2 == 0:
#         filtered.append(n)
#     elif command == "odd" and n % 2 != 0:
#         filtered.append(n)
#     elif command == "negative" and n < 0:
#         filtered.append(n)
#     elif command == "positive" and n >= 0:
#         filtered.append(n)
#
# print(filtered)
