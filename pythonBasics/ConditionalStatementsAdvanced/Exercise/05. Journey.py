# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# •	Бюджет - реално число;
# •	Един от двата възможни сезона - "summer” или "winter”.

# •	При 100 лв. или по-малко – някъде в България:
# o	Лято – 30% от бюджета;
# o	Зима – 70% от бюджета.
# •	При 1000 лв. или по малко – някъде на Балканите:
# o	Лято – 40% от бюджета;
# o	Зима – 80% от бюджета.
# •	При повече от 1000 лв. – някъде из Европа:
# o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.

budget = float(input())
seasons = input()

price = 0
destination = ''
accommodation = ''

if budget <= 100:
    destination = 'Bulgaria'
    if seasons == 'summer':
        accommodation = 'Camp'
        price = budget * 0.3
    else:
        accommodation = 'Hotel'
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if seasons == 'summer':
        accommodation = 'Camp'
        price = budget * 0.4
    else:
        accommodation = 'Hotel'
        price = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    accommodation = 'Hotel'
    price = budget * 0.9

print(f'Somewhere in {destination}\n{accommodation} - {price:.2f}')
