# Програмата прочита 3 числа, въведени от потребителя, на отделни редове:
# •	Възрастта на Лили - цяло число в интервала [1...77]
# •	Цената на пералнята - число в интервала [1.00...10 000.00]
# •	Единична цена на играчка - цяло число в интервала [0...40]

age = int(input())
washer_price = float(input())
toy_price = int(input())

saved_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        saved_money += (year * 10 / 2) - 1
    else:
        saved_money += toy_price

diff = abs(saved_money - washer_price)

if saved_money >= washer_price:

    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
