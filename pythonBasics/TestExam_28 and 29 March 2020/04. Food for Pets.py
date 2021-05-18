days = int(input())
food_total = float(input())

sum_dog_food = 0
sum_cat_food = 0
total_food_eaten = 0
biscuits = 0

for day in range(1, days + 1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    sum_dog_food += dog_eaten_food  # hranata izqdena ot kucheto
    sum_cat_food += cat_eaten_food  # hranata izqdena ot kotkata
    total_food_eaten = sum_cat_food + sum_dog_food  # obshto hranata izqdena prez dnite ot dvete
    if day % 3 == 0:
        current_biscuits = (cat_eaten_food + dog_eaten_food) * 0.1
        biscuits += current_biscuits

print(f'Total eaten biscuits: {round(biscuits)}gr.')
print(f'{(total_food_eaten * 100) / food_total:.2f}% of the food has been eaten.')
print(f'{(sum_dog_food * 100) / total_food_eaten:.2f}% eaten from the dog.')
print(f'{(sum_cat_food * 100) / total_food_eaten:.2f}% eaten from the cat.')
