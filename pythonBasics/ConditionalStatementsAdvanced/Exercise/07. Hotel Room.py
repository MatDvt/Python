# Предлагат се и следните отстъпки:
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

# •	На първия ред е месецът – May, June, July, August, September или October;
# •	На втория ред е броят на нощувките – цяло число.

months = input()
nights = int(input())

studio_price = 0
apartment_price = 0

if months == 'May' or months == 'October':
    studio_price = nights * 50
    apartment_price = nights * 65
    if 7 < nights < 14:
        studio_price -= studio_price * 0.05
    elif nights > 14:
        studio_price -= studio_price * 0.3
        apartment_price -= apartment_price * 0.1
elif months == 'June' or months == 'September':
    studio_price = nights * 75.20
    apartment_price = nights * 68.70
    if nights > 14:
        studio_price -= studio_price * 0.2
        apartment_price -= apartment_price * 0.1
elif months == 'July' or months == 'August':
    studio_price = nights * 76
    apartment_price = nights * 77
    if nights > 14:
        apartment_price -= apartment_price * 0.1

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
