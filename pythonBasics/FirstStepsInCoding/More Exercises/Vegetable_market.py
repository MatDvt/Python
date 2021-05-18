vegetable_price = float(input())
fruit_price = float(input())
vegetable_quantity = int(input())
fruit_quantity = int(input())

income = ((vegetable_price * vegetable_quantity) + (fruit_price * fruit_quantity)) / 1.94
print('{:.2f}'.format(income))
