group_climbers = int(input())

all_climbers = 0
mus = 0
monb = 0
kili = 0
k2 = 0
ev = 0
for climbers in range(1, group_climbers + 1):
    people = int(input())
    all_climbers += people

    if people <= 5:
        current_mus = 0
        current_mus += people
        mus += current_mus
    if 6 <= people <= 12:
        current_monb = 0
        current_monb += people
        monb += current_monb
    if 13 <= people <= 25:
        current_kili = 0
        current_kili += people
        kili += current_kili
    if 26 <= people <= 40:
        current_k2 = 0
        current_k2 += people
        k2 += current_k2
    if people >= 41:
        current_ev = 0
        current_ev += people
        ev += current_ev

print(f'{(mus / all_climbers) * 100:.2f}%')
print(f'{(monb / all_climbers) * 100:.2f}%')
print(f'{(kili / all_climbers) * 100:.2f}%')
print(f'{(k2 / all_climbers) * 100:.2f}%')
print(f'{(ev / all_climbers) * 100:.2f}%')
