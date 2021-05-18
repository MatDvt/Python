products_lst = input().split()
searched_products = input().split()
products_dict = {}

for ind in range(0, len(products_lst), 2):
    current_ind = products_lst[ind]
    current_value = int(products_lst[ind + 1])
    products_dict[current_ind] = current_value

for s_products in searched_products:
    if s_products in products_dict:
        print(f"We have {products_dict[s_products]} of {s_products} left")
    else:
        print(f"Sorry, we don't have {s_products}")


.3




