coffees = input().split()

num_commands = int(input())

for n in range(num_commands):
    command = input().split()
    current_command = command

    if command[0] == 'Include':
        coff = current_command[1]
        coffees.append(coff)

    elif command[0] == 'Remove':
        if command[1] == 'first':
            coff_to_remove = command[2]
            coff_to_remove = int(coff_to_remove)
            for i in range(coff_to_remove):
                del coffees[0]
        elif command[1] == 'last':
            coff_to_remove = command[2]
            coff_to_remove = int(coff_to_remove)
            for i in range(coff_to_remove):
                del coffees[-1]

    elif command[0] == 'Prefer':
        f_indx = command[1]
        f_indx = int(f_indx)
        s_indx = command[2]
        s_indx = int(s_indx)
        if len(coffees) > f_indx >= 0 and len(coffees) > s_indx >= 0:
            coffees[f_indx], coffees[s_indx] = coffees[s_indx], coffees[f_indx]

    else:
        list.reverse(coffees)

print(f"Coffees:")
print(" ".join(coffees))
