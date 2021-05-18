all_materials = input()

# a dictionary to hold the legendaries to ease the print process instead of creating multi checks
legendaries = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}

key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
is_obtained = False

while not is_obtained:
    split_data = all_materials.split()

    for index in range(0, len(split_data), 2):
        if is_obtained:
            break

        quantity = int(split_data[index])
        material = split_data[index + 1].lower()  # to lower since the input is caps and lower

        if material in key_materials:
            key_materials[material] += quantity
        else:
            if material not in junk_materials:
                junk_materials[material] = quantity
            else:
                junk_materials[material] += quantity

        for material, quantity in key_materials.items():
            if quantity >= 250:
                is_obtained = True  # get out of the loop once one of the items is obtained
                key_materials[material] -= 250
                print(f"{legendaries[material]} obtained!")
                break
    if is_obtained:
        break
    all_materials = input()

# sorting the key materials left in descending order by quantity and if two has the same quantity, sorting in
# alphabetical order

sorted_items = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))  # dont forget that this is a tuple
for material, quantity in sorted_items:
    print(f"{material}: {quantity}")

sorted_junks = sorted(junk_materials.items(), key=lambda kvp: kvp[0])  # sorting ascending alphabetical
for material, quantity in sorted_junks:
    print(f"{material}: {quantity}")
