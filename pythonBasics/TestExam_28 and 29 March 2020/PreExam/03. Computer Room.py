# Входът се чете от конзолата и съдържа точно 4 реда:
# •	На първия ред - месецът - текст с възможности: "march", "april", "may", "june", "july", "august"
# •	На втория ред - броят на прекараните часове - цяло число в диапазона [1...10]
# •	На третия ред - броят на хората в групата -  цяло число в диапазона [1...10]
# •	На четвъртия ред - времето от деня – текст с възможности: "day", "night"

month = input()
hours_spent = int(input())
people = int(input())
time_of_the_day = input()

total_price_per_day = 0
price_per_person = 0

if month == 'march' or month == 'april' or month == 'may':
    if time_of_the_day == 'day':
        price_per_person = 10.50
        total_price_per_day = (10.50 * hours_spent) * people
        if people >= 4 and hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.1)
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif people >= 4:
            price_per_person = price_per_person - (price_per_person * 0.1)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people

    if time_of_the_day == 'night':
        price_per_person = 8.40
        total_price_per_day = (8.40 * hours_spent) * people
        if people >= 4 and hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.1)
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif people >= 4:
            price_per_person = price_per_person - (price_per_person * 0.1)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people


elif month == 'june' or month == 'july' or month == 'august':
    if time_of_the_day == 'day':
        price_per_person = 12.60
        total_price_per_day = (12.60 * hours_spent) * people
        if people >= 4 and hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.1)
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif people >= 4:
            price_per_person = price_per_person - (price_per_person * 0.1)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people

    if time_of_the_day == 'night':
        price_per_person = 10.20
        total_price_per_day = (10.20 * hours_spent) * people
        if people >= 4 and hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.1)
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif people >= 4:
            price_per_person = price_per_person - (price_per_person * 0.1)
            total_price_per_day = (price_per_person * hours_spent) * people
        elif hours_spent >= 5:
            price_per_person = price_per_person - (price_per_person * 0.5)
            total_price_per_day = (price_per_person * hours_spent) * people

print(f'Price per person for one hour: {price_per_person:.2f}')
print(f'Total cost of the visit: {total_price_per_day:.2f}')
