#Write a program that reads a floating-point number and prints "zero" if the number is zero.
# #Otherwise, print "positive" or "negative". #
# Add "small" if the absolute value of the number is less than 1, or "large" if it exceeds 1 000 000.

num1 = float(input())

if num1 == 0:
    print(f'zero')
elif num1 > 0:
    if num1 < 1:
        print(f'small positive')
    elif num1 > 1000000:
        print(f'large positive')
    else:
        print(f'positive')
else:
    if abs(num1) < 1:
        print(f'small negative')
    elif abs(num1) > 1000000:
        print(f'large negative')
    else:
        print(f'negative')