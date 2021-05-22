# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  –  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  –  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  –  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка, която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата – цяло число;
# •	Сезон –  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари – цяло число.

budget = int(input())
season = input()
fisherman = int(input())

rent = 0

if season == 'Spring':
    rent = 3000
elif season == 'Summer' or season == 'Autumn':
    rent = 4200
elif season == 'Winter':
    rent = 2600

if fisherman <= 6:
    rent -= rent * 0.1
elif fisherman <= 11:
    rent -= rent * 0.15
else:
    rent -= rent * 0.25

if fisherman % 2 == 0 and not season == 'Autumn':
    rent -= rent * 0.05

diff = abs(budget - rent)
if budget >= rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')