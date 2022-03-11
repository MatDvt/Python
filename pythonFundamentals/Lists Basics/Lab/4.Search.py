# num = int(input())
# searched_word = input()
# words = []
# filtered_words = []
#
# for word in range(num):
#     curr_expression = input()
#     words.append(curr_expression)
#     if searched_word in curr_expression:
#         filtered_words.append(curr_expression)
# print(words)
# print(filtered_words)


# Using a function

num = int(input())
searched_word = input()


def search(n, searched):
    words = []
    filtered_words = []
    for j in range(n):
        c_exp = input()
        words.append(c_exp)
        if searched in c_exp:
            filtered_words.append(c_exp)
    print(words)
    print(filtered_words)


search(num, searched_word)
