#	Декорът за филма е на стойност 10% от бюджета.
#	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

# На конзолата трябва да се отпечатат два реда:
# •	Ако  парите за декора и дрехите са повече от бюджета:
# o	"Not enough money!"
# o	"Wingard needs {парите недостигащи за филма} leva more."
#	Ако парите за декора и дрехите са по малко или равни на бюджета:
# o	"Action!"
# o	"Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.

budget = float(input())
statists = int(input())
price_per_statist = float(input())

decor = budget * 0.1
price_all_statists = statists * price_per_statist
movie_price = decor + price_all_statists

if statists >= 150:
    price_all_statists -= price_all_statists * 0.1
    movie_price = decor + price_all_statists
if movie_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {movie_price - budget:.2f} leva more.')
elif movie_price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {budget - movie_price:.2f} leva left.')
