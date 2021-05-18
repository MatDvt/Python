import math

biscuits_per_worker = int(input())
workers = int(input())
competing_factory = int(input())

production_per_month = 0

for day in range(1, 31):
    daily_production = 0
    if day % 3 == 0:
        daily_production = math.floor((workers * biscuits_per_worker) * 0.75)
    else:
        daily_production = math.floor(workers * biscuits_per_worker)
    production_per_month += daily_production

print(f'You have produced {int(production_per_month)} biscuits for the past month.')

difference = abs(production_per_month - competing_factory)
percentage = (difference / competing_factory) * 100

if production_per_month >= competing_factory:
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    print(f'You produce {percentage:.2f} percent less biscuits.')