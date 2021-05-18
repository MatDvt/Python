# 1.	dog -> mammal
# 2.	crocodile, tortoise, snake -> reptile
# 3.	others -> unknown


animal = input()

if animal == 'dog':
    print('mammal')
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    print('reptile')
else:
    print('unknown')
