# От конзолата се четaт два реда:
# •	Брой дни – цяло число в интервала [1 … 5]
# •	Брой часове за всеки един от дните - цяло число в интервала [1 … 24]

days = int(input())
hours = int(input())
total_sum = 0

for day in range(1, days + 1):
    sum_per_day = 0  # sumata za vseki den
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 == 1:
            sum_per_day += 2.50
        elif day % 2 == 1 and hour % 2 == 0:
            sum_per_day += 1.25
        else:
            sum_per_day += 1
    print(f'Day: {day} - {sum_per_day:.2f} leva')
    total_sum += sum_per_day
print(f'Total: {total_sum:.2f} leva')
