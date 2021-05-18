#	Торта  – цената ѝ е 20% от наема на залата
#	Напитки – цената им е 45% по-малко от тази на тортата
#	Аниматор – цената му е 1/3 от цената за наема на залата

hall_rent = int(input())

cake = hall_rent * 0.2
drinks = cake - (cake * 0.45)
animator = hall_rent / 3

sum = hall_rent + cake + drinks + animator
print(sum)
