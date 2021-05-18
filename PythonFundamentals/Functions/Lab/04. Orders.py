def order_price(prd, q):
    if prd == "coffee":
        return q * 1.50
    elif prd == "coke":
        return q * 1.40
    elif prd == "water":
        return q * 1
    elif prd == "snacks":
        return q * 2.00


product = input()
quantity = int(input())
result = order_price(product, quantity)
print(f"{result:.2f}")
