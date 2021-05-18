# От конзолата се четат 5 реда:
# 1.	Име на филм - текст
# 2.	Брой дни - цяло число в диапазона [1… 90]
# 3.	Брой билети  - цяло число в диапазона [100… 100000]
# 4.	Цена на билет - реално число в диапазона [5.0… 25.0]
# 5.	Процент за киното - цяло число в диапазона [5... 35]

movie_name = input()
count_days = int(input())
count_tickets = int(input())
ticket_price = float(input())
percent = int(input())

sum_all_tickets_per_day = count_tickets * ticket_price
sum_all_days = sum_all_tickets_per_day * count_days
sum_for_cinema = percent / 100 * sum_all_days
profit = sum_all_days - sum_for_cinema

print(f'The profit from the movie {movie_name} is {profit:.2f} lv.')
