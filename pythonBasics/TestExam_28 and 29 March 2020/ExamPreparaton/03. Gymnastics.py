# Входът се чете от конзолата и се състои от два реда:
# •	Първи ред – държава – текст ("Russia", "Bulgaria" или "Italy")
# •	Втори ред – уред - текст ("ribbon", "hoop" или "rope")

country = input()
sport = input()

sum_grades = 0
difficulty = 0
performance = 0
# sum_grades = difficulty + performance


if country == 'Bulgaria' and sport == 'ribbon':
    difficulty = 9.600
    performance = 9.400
    sum_grades = difficulty + performance
elif country == 'Bulgaria' and sport == 'hoop':
    difficulty = 9.550
    performance = 9.750
    sum_grades = difficulty + performance
elif country == 'Bulgaria' and sport == 'rope':
    difficulty = 9.500
    performance = 9.400
    sum_grades = difficulty + performance

elif country == 'Russia' and sport == 'ribbon':
    difficulty = 9.100
    performance = 9.400
    sum_grades = difficulty + performance
elif country == 'Russia' and sport == 'hoop':
    difficulty = 9.300
    performance = 9.800
    sum_grades = difficulty + performance
elif country == 'Russia' and sport == 'rope':
    difficulty = 9.600
    performance = 9.000
    sum_grades = difficulty + performance

elif country == 'Italy' and sport == 'ribbon':
    difficulty = 9.200
    performance = 9.500
    sum_grades = difficulty + performance
elif country == 'Italy' and sport == 'hoop':
    difficulty = 9.450
    performance = 9.350
    sum_grades = difficulty + performance
elif country == 'Italy' and sport == 'rope':
    difficulty = 9.700
    performance = 9.150
    sum_grades = difficulty + performance

percent = ((20 - sum_grades) / 20) * 100

print(f'The team of {country} get {sum_grades:.3f} on {sport}.')
print(f'{percent:.2f}%')
