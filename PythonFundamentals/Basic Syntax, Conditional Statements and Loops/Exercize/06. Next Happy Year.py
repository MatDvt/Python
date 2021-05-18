#You're saying good-bye your best friend, "See you next happy year".#
# Happy Year is the year with only distinct digits, (e.g) 2018.
# #Write a program that receives an integer number and finds the next happy year.

# learn how to use  SET

year = int(input())

while True:
    year += 1
    next_year = str(year)
    if len(next_year) == len(set(next_year)):
        print(year)
        break
