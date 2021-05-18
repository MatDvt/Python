product_lst = input().split("|")

data_command = input()

while not data_command == "Shop!":
    command = data_command.split("%")
    if command[0] == "Important":
        product = command[1]
        if product in product_lst:
            product_lst.insert(0, product_lst.pop(product_lst.index(product))) # replace elements in a list
        else:
            product_lst[:0] = [product]

    elif command[0] == "Add":
        product = command[1]
        if product in product_lst:
            print("The product is already in the list")
        else:
            product_lst.append(product)

    elif command[0] == "Swap":
        product = command[1]
        product2 = command[2]

        if product in product_lst and product2 in product_lst:
            p1_ind = product_lst.index(product)
            p2_ind = product_lst.index(product2)

            product_lst[p1_ind], product_lst[p2_ind] = product_lst[p2_ind], product_lst[p1_ind]

        elif product not in product_lst:
            print(f"Product {product} missing!")

        elif product2 not in product_lst:
            print(f"Product {product2} missing!")

    elif command[0] == "Remove":
        product = command[1]
        if product in product_lst:
            product_lst.remove(product)
        else:
            print(f"Product {product} isn't in the list.")

    data_command = input()

for idx, val in enumerate(product_lst):
    print(f"{idx + 1}. {val}")
