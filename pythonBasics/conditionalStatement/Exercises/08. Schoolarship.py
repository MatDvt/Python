# социална стипендия
# доход на член от семейството по-малък от минималната работна заплата и успех над 4.5
# Размер на социалната стипендия - 35% от минималната работна заплата

# стипендия за отличен успех
# успех над 5.5, включително
# Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.

# 1.	Доход в лева - реално число;
# 2.	Среден успех -  реално числсо;
# 3.	Минимална работна заплата – реално число.
import math

income = float(input())
grade = float(input())
salary = float(input())

excellent_schoolarhip = 0
social_schoolarship = 0

if grade >= 5.50:
    excellent_schoolarhip += grade * 25
if income < salary and grade > 4.50:
    social_schoolarship += salary * 0.35

if social_schoolarship > excellent_schoolarhip:
    print(f'You get a Social scholarship {math.floor(social_schoolarship)} BGN')
elif excellent_schoolarhip >= social_schoolarship:
    if excellent_schoolarhip != 0:
        print(f'You get a scholarship for excellent results {math.floor(excellent_schoolarhip)} BGN')
    else:
        print(f'You cannot get a scholarship!')
