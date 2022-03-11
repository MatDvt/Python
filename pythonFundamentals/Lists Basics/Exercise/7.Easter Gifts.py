list_of_gifts = input().split()
command = input()

while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for current_index in range(len(list_of_gifts)):
            if list_of_gifts[current_index] == current_gift:
                list_of_gifts[current_index] = "None"
    elif current_command[0] == "Required":
        this_index = int(current_command[2])
        if 0 <= this_index < len(list_of_gifts):
            list_of_gifts[this_index] = current_gift
    elif current_command[0] == "JustInCase":
        list_of_gifts[-1] = current_gift

    command = input()

for gift in list_of_gifts:
    if gift != "None":
        print(gift, end=" ")
