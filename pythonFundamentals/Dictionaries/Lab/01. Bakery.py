grocery = input().split()
products = {}

for index in range(0, len(grocery), 2):
    current_product = grocery[index]
    current_value = int(grocery[index + 1])
    products[current_product] = current_value

print(products)
