# Вход
# От конзолата се четат 3 реда:
# 1.	Плод - текст с възможности: "Watermelon", "Mango", "Pineapple" или "Raspberry"
# 2.	Размерът на сета - текст с възможности: "small" или "big"
# 3.	Брой на поръчаните сетове - цяло число в интервала [1 … 10000]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Цената, която трябва да се заплати, форматирана до втория знак след десетичната запетая,
# в следния формат:
# "{цената} lv."

# 	                Диня 	       Манго	      Ананас	     Малина
# 2 броя (small)	56 лв./бр.	36.66 лв./бр.	42.10 лв./бр.	20 лв./бр.
# 5 броя (big)	28.70 лв./бр.	19.60 лв./бр.	24.80 лв./бр.	15.20 лв./бр.

# •	от 400 лв. до 1000 лв. включително има 15% отстъпка
# •	над 1000 лв. има 50% отстъпка

flavour = input()
pack_size = input()
set_count = int(input())
price = 0

if flavour == 'Watermelon' and pack_size == 'small':
    price = (2 * 56) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Watermelon' and pack_size == 'big':
    price = (5 * 28.70) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Mango' and pack_size == 'small':
    price = (2 * 36.66) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Mango' and pack_size == 'big':
    price = (5 * 19.60) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Pineapple' and pack_size == 'small':
    price = (2 * 42.10) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Pineapple' and pack_size == 'big':
    price = (5 * 24.80) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

elif flavour == 'Raspberry' and pack_size == 'small':
    price = (2 * 20) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5


elif flavour == 'Raspberry' and pack_size == 'big':
    price = (5 * 15.20) * set_count
    if 400 <= price <= 1000:
        price = price - price * 0.15
    elif price > 1000:
        price = price - price * 0.5

print(f'{price:.2f} lv.')
