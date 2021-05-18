# От конзолата се чете:
# •	На първи ред – бюджетът - реално число в интервала [1.00… 100000.00]
# •	След това поредица от два реда (до получаване на команда "Stop" или
# при заявка за купуване на продукт, чиято стойност е по-висока от наличния бюджет) :
# o	Име на продукта – текст
# o	Цена на продукта – реално число в интервала [1.00… 5000.00]

budget = float(input())
product_name = input()

counter = 0
all_products_price = 0

while product_name != 'Stop':
    product_price = float(input())
    counter += 1
    if counter % 3 == 0:
        all_products_price += product_price / 2
    else:
        all_products_price += product_price

    if all_products_price > budget:
        print(f"You don't have enough money!")
        needed_money = all_products_price - budget
        print(f"You need {needed_money:.2f} leva!")
        break

    product_name = input()

else:
    print(f'You bought {counter} products for {all_products_price:.2f} leva.')
