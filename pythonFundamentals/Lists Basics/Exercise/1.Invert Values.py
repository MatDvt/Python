# WITHOUT A FUNCTION

# nums = input().split(" ")
#
# opposite = []
# for i in nums:
#     cur_ind = int(i)
#     neg_i = -cur_ind
#     opposite.append(neg_i)
#
# print(opposite)


# USING A FUNCTION

nums = input().split(" ")

opposite = []


def invert(numbers):
    for num in numbers:
        cur_num = int(num)
        neg_num = - cur_num
        opposite.append(neg_num)
    print(opposite)


invert(nums)
