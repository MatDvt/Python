# Входът от конзолата съдържа 5 реда:
# •	Цена за отпечатване на една страница - реално число в интервала (0.00…1.50]
# •	Цена за отпечатване на една корица - реално число в интервала (0.00…5.00]
# •	Процентно намаление за отпечатване на хартия - цяло число в интервала (0…100]
# •	Сумата, която трябва да се заплати на дизайнер - реално число в интервала (0.00…150.00]
# •	Процент от цялата дължима сума, който е заплатен от екипа - цяло число в интервала [0…100]

price_per_page = float(input())
price_per_cover = float(input())
percent_for_print_on_paper = int(input())
pay_for_designer = float(input())
percent_paid_by_the_team = int(input())

total_sum_pages = price_per_page * 899
total_sum_cover = price_per_cover * 2
total_sum_book = total_sum_cover + total_sum_pages
discount_price = total_sum_book - ((total_sum_book * percent_for_print_on_paper) / 100)
discount_price += pay_for_designer
discount_price = discount_price - ((discount_price * percent_paid_by_the_team) / 100)
print(f'Avtonom should pay {discount_price:.2f} BGN.')
