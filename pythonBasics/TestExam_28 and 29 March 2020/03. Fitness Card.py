money = float(input())
sex = input()
age = int(input())
sport = input()

price = 0

if sex == 'm' and sport == 'Gym':
    price = 42
    if age <= 19:
        price = price - price * 0.2

elif sex == 'm' and sport == 'Boxing':
    price = 41
    if age <= 19:
        price = price - price * 0.2

elif sex == 'm' and sport == 'Yoga':
    price = 45
    if age <= 19:
        price = price - price * 0.2

elif sex == 'm' and sport == 'Zumba':
    price = 34
    if age <= 19:
        price = price - price * 0.2

elif sex == 'm' and sport == 'Dances':
    price = 51
    if age <= 19:
        price = price - price * 0.2

elif sex == 'm' and sport == 'Pilates':
    price = 39
    if age <= 19:
        price = price - price * 0.2

# women

if sex == 'f' and sport == 'Gym':
    price = 35
    if age <= 19:
        price = price - price * 0.2

elif sex == 'f' and sport == 'Boxing':
    price = 37
    if age <= 19:
        price = price - price * 0.2

elif sex == 'f' and sport == 'Yoga':
    price = 42
    if age <= 19:
        price = price - price * 0.2

elif sex == 'f' and sport == 'Zumba':
    price = 31
    if age <= 19:
        price = price - price * 0.2

elif sex == 'f' and sport == 'Dances':
    price = 53
    if age <= 19:
        price = price - price * 0.2

elif sex == 'f' and sport == 'Pilates':
    price = 37
    if age <= 19:
        price = price - price * 0.2
if price <= money:
    print(f'You purchased a 1 month pass for {sport}.')
else:
    print(f'You don\'t have enough money! You need ${abs(money - price):.2f} more.')
