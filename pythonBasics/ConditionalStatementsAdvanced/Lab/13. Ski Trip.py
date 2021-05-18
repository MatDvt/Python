# •	Първи ред - дни за престой - цяло число;
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment";

days = int(input())
room = input()
grade = input()

price_room = 18
price_apartment = 25
price_suite = 35

if room == 'room for one person':
    price = (days - 1) * price_room
    if grade == 'positive':
        price = price + (price * 0.25)
        print(f'{price:.2f}')
    else:
        price = price - (price * 0.1)
        print(f'{price:.2f}')
elif room == 'apartment':
    if days < 10:
        price = ((days - 1) * price_apartment)
        price = price - (price * 0.3)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')
    elif 10 < days <= 15:
        price = (days - 1) * price_apartment
        price = price - (price * 0.35)
        # print(price)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')
    elif days > 15:
        price = ((days - 1) * price_apartment)
        price = price - (price * 0.5)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')

elif room == 'president apartment':
    if days < 10:
        price = (days - 1) * price_suite
        price = price - (price * 0.1)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')
    elif 10 < days <= 15:
        price = (days - 1) * price_suite
        price = price - (price * 0.15)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')
    elif days > 15:
        price = (days - 1) * price_suite
        price = price - (price * 0.2)
        if grade == 'positive':
            price = price + (price * 0.25)
            print(f'{price:.2f}')
        else:
            price = price - (price * 0.1)
            print(f'{price:.2f}')
