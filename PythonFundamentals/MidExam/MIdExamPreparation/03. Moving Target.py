# create a function to check for the index
def check_if_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


targets = [int(el) for el in input().split()]

main_command = input()

while not main_command == "End":
    command, index, val = main_command.split()  # we have the same input with 3 parameters hence we split them separately
    index = int(index)
    val = int(val)

    if command == "Shoot":
        if check_if_index_is_valid(index, len(targets)):
            targets[index] -= val
            if targets[index] <= 0:
                targets.pop(index)

    elif command == "Add":
        if check_if_index_is_valid(index, len(targets)):
            targets.insert(index, val)  # add/insert a value in the list by given index and value
        else:
            print(f'Invalid placement!')

    elif command == "Strike":
        left_most_index = index - val  # get radius on the left side from the given index
        right_most_index = index + val  # like the one above but to the right
        if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(
                targets)) and check_if_index_is_valid(right_most_index, len(targets)):
            unshot_left_half = targets[:left_most_index]  # we take the one that's not going to be shot
            unshot_right_half = targets[right_most_index + 1:] # not including the right most one (+1)
            targets = unshot_left_half + unshot_right_half
        else:
            print("Strike missed!")
    main_command = input()
print('|'.join([str(el) for el in targets]))
