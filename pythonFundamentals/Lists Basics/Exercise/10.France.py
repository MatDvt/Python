items = input().split("|")
budget = float(input())
total_bought = []
profit = 0

for item in items:
    indx = item.split('->')
    clothes = indx[0]
    price = float(indx[1])

    is_accepted = False

    if price > budget:
        continue

    if clothes == 'Clothes':
        if price <= 50.00:
            budget -= price
            is_accepted = True
    elif clothes == 'Shoes':
        if price <= 35.00:
            budget -= price
            is_accepted = True
    elif clothes == 'Accessories':
        if price <= 20.50:
            budget -= price
            is_accepted = True
    if is_accepted:
        res = float("{:.2f}".format(price * 1.40))
        total_bought.append(price * 1.40)
        profit += (price * 1.40) - price

for ele in total_bought:
    budget += ele


def l_to_s(s):
    str1 = ''
    for element in s:
        str1 += "{:.2f}".format(element) + " "
    return str1


print(l_to_s(total_bought))
print(f'Profit: {profit:.2f}')

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')