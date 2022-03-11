n = int(input())

lst_pos = []
lst_neg = []


def calc_neg_pos(nums):
    count_pos = 0
    sum_neg = 0
    for num in range(n):
        cur_num = int(input())
        if cur_num >= 0:
            lst_pos.append(cur_num)
            count_pos += 1
        else:
            lst_neg.append(cur_num)
            sum_neg += cur_num
    print(lst_pos)
    print(lst_neg)
    print(f'Count of positives: {count_pos}\nSum of negatives: {sum_neg}')


calc_neg_pos(n)


