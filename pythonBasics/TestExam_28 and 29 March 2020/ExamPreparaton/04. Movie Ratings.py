# От конзолата първо се чете един ред:
# •	Брой филми, които си е набелязала Деси – цяло число в интервала [1…20]
# За всеки филм се прочитат два отделни реда:
# •	Име на филма – текст
# •	Рейтинг на филма - реално число в интервала [1.00…10.00]
import sys

count_movies = int(input())
# movie_name = input()
# rating = float(input())

sum_rating = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
max_current_movie = ''
min_current_movie = ''

for movie in range(1, count_movies + 1):
    movie_name = input()
    rating = float(input())
    sum_rating += rating
    if rating > max_rating:
        max_rating = rating
        max_current_movie = movie_name
    if rating < min_rating:
        min_rating = rating
        min_current_movie = movie_name

average_rating = sum_rating / count_movies

print(f'{max_current_movie} is with highest rating: {max_rating:.1f}')
print(f'{min_current_movie} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')
