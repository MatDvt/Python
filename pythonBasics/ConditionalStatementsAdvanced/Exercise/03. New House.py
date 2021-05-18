# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# •	Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# •	Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0

if flower_type == 'Roses':
    price = 5
    if flower_count > 80:
        price -= price * 0.1
elif flower_type == 'Dahlias':
    price = 3.8
    if flower_count > 90:
        price -= price * 0.15
elif flower_type == 'Tulips':
    price = 2.8
    if flower_count > 80:
        price -= price * 0.15
elif flower_type == 'Narcissus':
    price = 3
    if flower_count < 120:
        price += price * 0.15
elif flower_type == 'Gladiolus':
    price = 2.5
    if flower_count < 80:
        price += price * 0.2

money_needed = flower_count * price
diff = budget - money_needed
if budget >= money_needed:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {abs(diff):.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(diff):.2f} leva more.')
