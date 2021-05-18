# Първоначално от конзолата се прочита броят на авиокомпаниите – цяло число в интервала [1… 20]
# След това за всяка авиокомпания се прочита:
# •	Името на авиокомпанията – текст
# •	До получаване на командата "Finish" се чете:
# o	Брой пътници на полет  – цяло число в интервала [1... 360]

air_companies = int(input())
air_name = input()

all_passengers = 0
counter = 0
for i in range(1, air_companies + 1):
    while air_name != 'Finish':
        passengers = int(input())
        all_passengers += passengers
        current_name = air_name
        counter += 1
        print(f'{air_name}: {all_passengers / counter} passengers.')

        air_name = input()
