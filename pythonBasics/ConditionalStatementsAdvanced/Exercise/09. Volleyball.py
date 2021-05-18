# Напишете програма, която изчислява колко пъти Влади е играл волейбол през годината.
# Закръглете резултата надолу до най-близкото цяло число (например 2.15  2; 9.95  9).
# Входните данни се въвеждат от потребителя, в следния вид:
# •	Първият ред съдържа думата "leap" (високосна година) или "normal" (невисокосна);
# •	Вторият ред съдържа цялото число p – брой празници в годината (които не са събота и неделя);
# •	Третият ред съдържа цялото число h – брой уикенди, в които Влади си пътува до родния град.

import math

year = input()
p = int(input())  # holidays
h = int(input())  # weekends home

free_weekends = 48 - h
weekends_sofia = free_weekends * 0.75
games_home = h
games_sofia = p * (2 / 3)
games_sum = weekends_sofia + games_sofia + games_home

if year == "leap":
    games_sum *= 1.15

print(math.floor(games_sum))
