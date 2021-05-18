def check_index_is_valid(index, lst_len):
    if index in range(lst_len):
        return True
    return False


cards = input().split()

command = input()
rounds = 0

while not command == "end" and cards:
    index_1, index_2 = command.split()  # get the indexes from the input
    index_1 = int(index_1)
    index_2 = int(index_2)

    rounds += 1

    # check if the index is in range as well as the provided indexes are not equal to each other
    if check_index_is_valid(index_1, len(cards)) and check_index_is_valid(index_2,
                                                                          len(cards)) and not index_1 == index_2:
        el_1 = cards[index_1]  # get the element of the list by the provided index
        el_2 = cards[index_2]
        if el_1 == el_2:
            cards.remove(el_1)
            cards.remove(el_2)
            print(f"Congrats! You have found matching elements - {el_1}!")
        else:
            print(f"Try again!")
    else:
        element_to_add = f"-{rounds}a"
        middle = len(cards) // 2  # get the mid of the list where we will be adding the element
        cards.insert(middle, element_to_add)
        cards.insert(middle, element_to_add)
        print(f"Invalid input! Adding additional elements to the board")

    command = input()

if not cards:
    print(f"You have won in {rounds} turns!")

else:
    print(f"Sorry you lose :(")
    print(' '.join(cards))
