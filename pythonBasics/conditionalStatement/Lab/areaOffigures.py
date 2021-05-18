import math

figure_type = input()
if figure_type == 'square' or figure_type == 'circle':
    num = float(input())
elif figure_type == 'rectangle' or figure_type == 'triangle':
    num1 = float(input())
    num2 = float(input())

if figure_type == 'square':
    print('{:.3f}'.format((num * num)))
elif figure_type == 'circle':
    print('{:.3f}'.format((math.pi * (num * num))))
elif figure_type == 'rectangle':
    print('{:.3f}'.format((num1 * num2)))
    # print(f"{(num1*num2):f3}")
else:
    print('{:.3f}'.format((num1 * num2) / 2))
