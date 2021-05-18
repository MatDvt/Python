# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони. Има три вида прожекции с билети на различни цени:
# •	Premiere – премиерна прожекция, на цена 12.00 лева;
# •	Normal – стандартна прожекция, на цена 7.50 лева;
# •	Discount – прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете
# тип прожекция (текст),
# брой редове и
# брой колони в залата (цели числа

projection = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if projection == 'Premiere':
    income = cinema_capacity * 12
    print(f'{income:.2f} leva')
elif projection == 'Normal':
    income = cinema_capacity * 7.5
    print(f'{income:.2f} leva')
elif projection == 'Discount':
    income = cinema_capacity * 5
    print(f'{income:.2f} leva')
