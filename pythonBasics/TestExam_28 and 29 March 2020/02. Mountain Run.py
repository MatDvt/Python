# Вход
# От конзолата се четат 3 реда:
# 1.	Рекордът в секунди – реално число в интервала [0.00 … 100000.00]
# 2.	Разстоянието в метри – реално число в интервала [0.00 … 100000.00]
# 3.	Времето в секунди, за което изкачва 1 м. – реално число в интервала [0.00 … 1000.00]
# Изход
# Отпечатването на конзолата зависи от резултата:
# •	Ако Георги е подобрил рекорда отпечатваме:
# o	" Yes! The new record is {времето на Георги} seconds."
# •	Ако НЕ е подобрил рекорда отпечатваме:
# o	"No! He was {недостигащите секунди} seconds slower."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.

record = float(input())  # Рекордът в секунди – реално число в интервала [0.00 … 100000.00]
distance = float(input())  # Разстоянието в метри – реално число в интервала [0.00 … 100000.00]
time = float(input())  # Времето в секунди, за което изкачва 1 м. – реално число в интервала [0.00 … 1000.00]

dist_in_sec = distance * time
slow_down = (distance // 50) * 30
total_time = dist_in_sec + slow_down

if record > total_time:
    print(f'Yes! The new record is {total_time:.2f} seconds.')
else:
    print(f'No! He was {total_time - record:.2f} seconds slower.')
