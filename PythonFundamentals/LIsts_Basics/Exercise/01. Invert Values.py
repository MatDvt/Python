word_of_nums = input()
create_a_list = word_of_nums.split()

for i in range(0, len(create_a_list)):
    create_a_list[i] = int(create_a_list[i])


def convert(lst):
    return [-i for i in lst]


print(convert(create_a_list))
