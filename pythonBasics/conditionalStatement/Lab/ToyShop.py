# 1. Цена на екскурзията - реално число;
# 2. Брой пъзели - цяло число;
# 3. Брой говорещи кукли - цяло число;
# 4. Брой плюшени мечета - цяло число;
# 5. Брой миньони - цяло число;
# 6. Брой камиончета - цяло число.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена. От спечелените
# пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на
# екскурзия.

holiday_price = float(input())
puzzles_amount = int(input())
doll_amount = int(input())
bears_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

puzzles_price = puzzles_amount * 2.60
doll_price = doll_amount * 3
bears_price = bears_amount * 4.10
minions_price = minions_amount * 8.20
trucks_price = trucks_amount * 2

toys_amount = puzzles_amount + doll_amount + bears_amount + minions_amount + trucks_amount
earnings = puzzles_price + doll_price + bears_price + minions_price + trucks_price

if toys_amount >= 50:
    earnings = earnings - (earnings * 0.25)

if holiday_price < earnings:
    earnings = earnings - (earnings * 0.1)
    earnings = earnings - holiday_price
    print(f'Yes! {earnings:.2f} lv left.')
else:
    earnings = earnings - (earnings * 0.1)
    earnings = holiday_price - earnings
    print(f'Not enough money! {earnings:.2f} lv needed.')
