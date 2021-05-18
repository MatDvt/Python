budget = float(input())
flour_price_per_1kg = float(input())

pack_of_eggs_price = flour_price_per_1kg * 0.75
milk_price_1l = (flour_price_per_1kg * 0.25) + flour_price_per_1kg
milk_used_per1_price = milk_price_1l * 0.25
price_per_one_cozunak = milk_used_per1_price + pack_of_eggs_price + flour_price_per_1kg

colored_eggs = 0
cozunak_count = 0
current_coz_count = 0
lost_eggs = 0

while price_per_one_cozunak < budget:
    cozunak_count += 1
    colored_eggs += 3
    budget = budget - price_per_one_cozunak
    if cozunak_count % 3 == 0:
        current_coz_count = cozunak_count
        lost_eggs = current_coz_count - 2
        colored_eggs = colored_eggs - lost_eggs

print(f"You made {cozunak_count} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
