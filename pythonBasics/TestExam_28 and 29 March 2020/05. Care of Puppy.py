food = int(input())

eaten_food = 0
food_in_grams = food * 1000

meal = (input())
while meal != 'Adopted':
    eaten_food += int(meal)
    left_food = abs(food_in_grams - eaten_food)
    meal = (input())

if food_in_grams >= eaten_food:
    print(f'Food is enough! Leftovers: {left_food} grams.')
else:
    print(f'Food is not enough. You need {left_food} grams more.')
