# От конзолата се четат 3 реда:
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
import math

movie = input()
movie_length = int(input())
break_length = int(input())

time_for_lunch = break_length * 1 / 8
time_for_relax = break_length * 1 / 4
time_left = break_length - time_for_lunch - time_for_relax
diff = abs(movie_length - time_left)

if time_left >= movie_length:
    print(f'You have enough time to watch {movie} and left with {math.ceil(diff)} minutes free time.')
else:

    print(f'You don\'t have enough time to watch {movie}, you need {math.ceil(diff)} more minutes.')
