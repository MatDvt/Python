# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - дестинация - текст с възможности"France", "Italy" или "Germany"
# •	Втори ред - дати, през които си е резервирала екскурзията - текст  с възможности "21-23",
# "24-27" или "28-31"
# •	Трети ред - брой нощувки - цяло число в интервала [1… 100]
# Изход
# На конзолата трябва да се отпечата един ред:
# "Easter trip to {дестинация} : {разходи за екскурзията} leva."
# Разходите за екскурзията да бъдат форматирани до втората цифра след десетичния знак

destination = input()
dates = input()
nights = int(input())

expenses = 0
if destination == 'France' and dates == '21-23':
    expenses = nights * 30
elif destination == 'France' and dates == '24-27':
    expenses = nights * 35
elif destination == 'France' and dates == '28-31':
    expenses = nights * 40

# Italy
elif destination == 'Italy' and dates == '21-23':
    expenses = nights * 28
elif destination == 'Italy' and dates == '24-27':
    expenses = nights * 32
elif destination == 'Italy' and dates == '28-31':
    expenses = nights * 39

# Germany
elif destination == 'Germany' and dates == '21-23':
    expenses = nights * 32
elif destination == 'Germany' and dates == '24-27':
    expenses = nights * 37
elif destination == 'Germany' and dates == '28-31':
    expenses = nights * 43

print(f'Easter trip to {destination} : {expenses:.2f} leva.')
