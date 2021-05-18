#	Цена на ягодите в лева – реално число;
#	Количество на бананите в килограми – реално число;
#	Количество на портокалите в килограми – реално число;
#	Количество на малините в килограми – реално число;
#	Количество на ягодите в килограми – реално число.

strawberry_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())

raspberry_price = (strawberry_price / 2)
raspberry_final_price = raspberry_price * raspberry_quantity
banana_price = (raspberry_price - (raspberry_price * 0.8)) * banana_quantity
orange_price = (raspberry_price - (raspberry_price * 0.4)) * orange_quantity
strawberry_price = strawberry_quantity * strawberry_price

print(strawberry_price + raspberry_final_price + orange_price + banana_price)
