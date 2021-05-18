# От конзолата се прочитат 5 реда:
# •	пол - символ със следните възможности: 'm' за мъж и 'f' за жена
# •	тегло в килограми - реално число в интервала (0.00…800.00]
# •	височина в метри - реално число в интервала [0.00…3.00]
# •	възраст в години - цяло число в интервала [0…120]
# •	ниво на физическа активност - текст със следните възможности:
# sedentary, lightly active, moderately active, very active

# Формула за мъже:
# •	БНМ = 66 + (13.7 x тегло в килограми) + (5 x височина в сантиметри) - (6.8 x възрастта в години)
# Формула за жени:
# •	БНМ = 655 + (9.6 x тегло в килограми) + (1.8 x височина в сантиметри) - (4.7 x възрастта в години)
# Ниво на активност и коефициенти, спрямо него:
# •	sedentary - заседнал начин на живот: БНМ се умножава по коефициент 1.2
# •	lightly active - слабо активен начин на живот: БНМ се умножава по коефициент 1.375
# •	moderately active - умерено активен начин на живот: БНМ се умножава по коефициент 1.55
# •	very active - много активен начин на живот: БНМ се умножава по коефициент 1.725
import math

sex = input()
weight = float(input())
height = float(input())
age = int(input())
phis_activity = input()

height_in_cm = height * 100

bnm = 0

if sex == 'm' and phis_activity == 'sedentary':
    bnm = (66 + (13.7 * weight) + (5 * height_in_cm) - (6.8 * age)) * 1.2
elif sex == 'm' and phis_activity == 'lightly active':
    bnm = (66 + (13.7 * weight) + (5 * height_in_cm) - (6.8 * age)) * 1.375
elif sex == 'm' and phis_activity == 'moderately active':
    bnm = (66 + (13.7 * weight) + (5 * height_in_cm) - (6.8 * age)) * 1.55
elif sex == 'm' and phis_activity == 'very active':
    bnm = (66 + (13.7 * weight) + (5 * height_in_cm) - (6.8 * age)) * 1.725

elif sex == 'f' and phis_activity == 'sedentary':
    bnm = (655 + (9.6 * weight) + (1.8 * height_in_cm) - (4.7 * age)) * 1.2
elif sex == 'f' and phis_activity == 'lightly active':
    bnm = (655 + (9.6 * weight) + (1.8 * height_in_cm) - (4.7 * age)) * 1.375
elif sex == 'f' and phis_activity == 'moderately active':
    bnm = (655 + (9.6 * weight) + (1.8 * height_in_cm) - (4.7 * age)) * 1.55
elif sex == 'f' and phis_activity == 'very active':
    bnm = (655 + (9.6 * weight) + (1.8 * height_in_cm) - (4.7 * age)) * 1.725

print(f'To maintain your current weight you will need {math.ceil(bnm)} calories per day.')
