# Според сайта се налагат различни глоби:
# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

# От конзолата се четат два реда:
# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [700...1500]
# След това n – на брой пъти се чете име на уебсайт – текст

tabs = int(input())
salary = int(input())

for i in range(tabs):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50

    if salary <= 0:
        print('You have lost your salary.')
        break
if salary > 0:
    print(salary)
