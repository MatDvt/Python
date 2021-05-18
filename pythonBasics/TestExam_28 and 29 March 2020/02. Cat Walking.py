# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред - минути разходка на ден - цяло число в интервала [1...50]
# •	На втория ред - броят на разходките дневно - цяло число в интервала [1…10]
# •	На третия ред - приетите от котката калории на ден – цяло число в интервала [100…4000]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако изгорените калории през разходката са повече или равни на  50% от приетите през деня калории:
# "Yes, the walk for your cat is enough. Burned calories per day: {общо изгорени калории от разходката}."
# •	Ако  изгорените калории през разходката са по-малко от 50% от приетите през деня калории:
#  "No, the walk for your cat is not enough. Burned calories per day: {общо изгорени калории от разходката}."

minutes_walk = int(input())
walk_count = int(input())
calories = int(input())

total_walks_in_mins = minutes_walk * walk_count
burned_calories = total_walks_in_mins * 5

needed_calories_per_day = calories * 0.5

if needed_calories_per_day <= burned_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}. ')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.')
