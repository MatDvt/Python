# Брой страници в текущата книга – цяло число
# Страници, които може да прочита за 1 час – цяло число
# Броя на дните, за които трябва да прочете книгата – цяло число


pages = int(input())
pages_per_hour = int(input())
days = int(input())

result = (pages / pages_per_hour) / days
print(result)
