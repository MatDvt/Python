# Ако покани:
# •	Между 10 (вкл.) и 15 (вкл.) човека -> 15 % отстъпка от куверта за един човек
# •	Между 15 и 20 (вкл.) човека -> 20 % отстъпка от куверта за един човек
# •	Над 20 човека -> 25 % отстъпка от куверта за един човек
# Деси трябва да предвиди и закупуването на торта за партито. Цената на тортата е 10% от бюджета на Деси.
# Напишете програма, която изчислява дали бюджетът на Деси ще и е достатъчен за партито.
# Вход
# От конзолата се четат 3 реда:
# 1.	Брой гости – цяло число в интервала [1...99]
# 2.	Цена на куверт за един човек – реално число в интервала [0.00 … 99.00]
# 3.	Бюджетът на Деси  – реално число в интервала [0.00 … 9999.00]

guests = int(input())
price_per_guest = int(input())
budget = float(input())
cake_price = budget * 0.1

if 10 <= guests <= 15:
    price_per_guest -= price_per_guest * 0.15
elif 15 < guests <= 20:
    price_per_guest -= price_per_guest * 0.20
elif guests > 20:
    price_per_guest -= price_per_guest * 0.25

price_all_guests = guests * price_per_guest + cake_price

if price_all_guests >= budget:
    print(f'No party! {price_all_guests - budget:.2f} leva needed.')
else:
    print(f'It is party time! {budget - price_all_guests:.2f} leva left.')
